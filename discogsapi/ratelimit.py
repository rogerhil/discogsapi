# Discogs API, Python Wrapper - https://www.discogs.com/developers/index.html
# Copyright (C) 2013 Rogerio Hilbert Lima <rogerhil@gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import re
import datetime
import externalip
import os
import tempfile

IP_REGEXP_STR = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"


class RateLimitException(Exception):
    pass


class RateLimitExceeded(Exception):
    pass


class RateLimit:
    """
    >>> import time
    >>> from discogsapi.ratelimit import RateLimit, RateLimitExceeded
    >>> RateLimit.RATE_LIMIT = 2   # Force limit to 2, just for this test
    >>> RateLimit.init_rate_limit_lock()
    >>> from discogsapi import Discogs
    >>> d = Discogs("HeyBaldock/1.0 +http://heybaldock.com.br")
    >>> image = d.images.get('R-150-63114-1148806222.jpeg')
    >>> resp = image.response
    >>> image = d.images.get('R-150-63114-1148806222.jpeg')
    >>> resp = image.response
    >>> image = d.images.get('R-150-63114-1148806222.jpeg')
    >>> err = None
    >>> try:
    ...    resp = image.response
    ... except RateLimitExceeded, err:
    ...    pass
    ...
    >>> assert err is not None
    >>> RateLimit.RATE_LIMIT_PERIOD_HOURS = (1.0 / 3600) * 5
    >>> time.sleep(5) # after RATE_LIMIT_PERIOD_HOURS the count begins again
    >>> image = d.images.get('R-150-63114-1148806222.jpeg')
    >>> resp = image.response
    """

    RATE_LIMIT = 1000 # this is default for Discogs API 2.0
    RATE_LIMIT_PERIOD_HOURS = 24 # this is default for Discogs API 2.0
    RATE_LIMIT_LOCK_FILE = 'discogs_rate_limit.lock'
    FORMAT_RATE_LIMIT_LOCK = '%(ip)s_%(datetime)s_%(count)s'
    REGEXP_RATE_LIMIT_LOCK = re.compile(r'^(%s)_(.+)_(\d+)$' % IP_REGEXP_STR)
    DATETIME_FORMAT = "%Y-%m-%dT%H:%M"

    @classmethod
    def _get_temp_file(cls, mode='r'):
        tmp = tempfile.gettempprefix()
        path = os.path.join('/', tmp, cls.RATE_LIMIT_LOCK_FILE)
        if mode == 'r' and not os.path.isfile(path):
            cls.init_rate_limit_lock()
        return open(path, mode)

    @classmethod
    def _read(cls):
        afile = cls._get_temp_file()
        content = afile.read()
        afile.close()
        return content

    @classmethod
    def _write(cls, data):
        afile = cls._get_temp_file('w')
        afile.write(data)
        afile.close()

    @classmethod
    def init_rate_limit_lock(cls):
        ip = externalip.get_external_ip()
        now = datetime.datetime.now()
        cls._write(cls._data_format(ip, now, 0))

    @classmethod
    def get_current_rate_limit_data(cls):
        content = cls._read()
        match = cls.REGEXP_RATE_LIMIT_LOCK.match(content)
        if not match:
            raise RateLimitException('Invalid rate limit data: %s' % content)
        ip, date_str, count_str = match.groups()
        date = datetime.datetime.strptime(date_str, cls.DATETIME_FORMAT)
        count = int(count_str)
        return ip, date, count

    @classmethod
    def _data_format(cls, ip, date, count, ip_updated=None):
        data = dict(
            ip=ip,
            datetime=date.strftime(cls.DATETIME_FORMAT),
            ip_updated=ip_updated or date,
            count=count
        )
        return cls.FORMAT_RATE_LIMIT_LOCK % data

    @classmethod
    def test_limit_and_increment(cls):
        now = datetime.datetime.now()
        hours = cls.RATE_LIMIT_PERIOD_HOURS
        oneday = datetime.timedelta(hours=hours)
        ip, date, count = cls.get_current_rate_limit_data()
        passed = now - date
        if passed < oneday:
            if count >= cls.RATE_LIMIT:
                passed_hours = passed.seconds / 3600
                remaining = hours - passed_hours
                msg = 'Rate limit exceeded %s downloads during %s hours. '\
                      'You can wait %s hours to manage to download again.' % \
                        (cls.RATE_LIMIT, passed_hours, remaining)
                raise RateLimitExceeded(msg)
        else:
            # restart the counting, since passed 24 hours
            cls.init_rate_limit_lock()
        count += 1
        cls._write(cls._data_format(ip, date, count))


if __name__ == "__main__":
    import doctest
    doctest.testmod()