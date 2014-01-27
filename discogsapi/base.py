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

""" Base module of Discogs API Python Wrapper.
    Contains the DiscogsBase class containing the methods for HTTP requests to
    the Discogs API.
"""

import urllib
import urllib2
from simplejson import loads


class DiscogsException(Exception):
    pass


class DiscogsBase(object):
    """ This is the base class for Discogs API.
        Contains the basic methods for HTTP requests to the Discogs API.
    """

    BASE_URL = 'http://api.discogs.com'

    def __init__(self, user_agent):
        """ The argument user_agent is required. Discogs API will block ips
        from requests with bad user_agent names.
        See the advise below from www.discogs.com/developers/accessing.html:
        "
        Your application must provide a User-Agent string that identifie
        itself - preferably something that follows RFC 1945. Some good
        examples include:
            AwesomeDiscogsBrowser/0.1 +http://adb.example.com
            LibraryMetadataEnhancer/0.3 +http://example.com/lime
            MyDiscogsClient/1.0 +http://mydiscogsclient.org

        Please don't just copy one of those! Make it unique so we can let you
        know if your application starts to misbehave - the alternative is that
        we just silently block it, which will confuse and infuriate your users.
        Here are some bad examples that are unclear or obscure the nature of
        the application:
            curl/7.9.8 (i686-pc-linux-gnu) libcurl 7.9.8 (OpenSSL 0.9.6b)
            Mozilla/5.0 (X11; Linux i686; rv:6.0.2) Gecko/20100101 Firefox/6.0
            my app
        "
        """
        self.user_agent = user_agent

    def get_response(self, path, params=None):
        """ Returns an addinfourl object response.
        path examples:
            /artists/45
            /artists/45/releases
            /masters/999
        """
        url = "%s%s" % (self.BASE_URL, path)
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        request = urllib2.Request(url)
        request.add_header('User-Agent', self.user_agent)
        request.get_method = lambda: 'GET'
        if params:
            request.add_data(urllib.urlencode(params))
        response = opener.open(request)
        return response

    def get_data(self, path, params=None):
        """ Returns a dict, parsed once through a json string.
        path examples **without** query string:
            /artists/45
            /artists/45/releases
            /masters/999
        """
        response = self.get_response(path, params=params)
        info = loads(response.read())
        return info

    def get_data_from_full_url(self, url):
        """ Returns a dict, parsed once through a json string.
        this path argument includes querystring:
            /artists/45/releases?page=2&per_page=20
        """
        p = urllib2.urlparse.urlparse(url)
        params = dict(urllib2.urlparse.parse_qsl(p.query))
        return self.get_data(p.path, params)
