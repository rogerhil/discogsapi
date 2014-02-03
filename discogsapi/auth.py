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

import urllib
import urllib2
from requests_oauthlib import OAuth1Session


class DiscogsAuth(object):

    REQUEST_TOKEN_URL = 'http://api.discogs.com/oauth/request_token'
    AUTHORIZE_URL = 'http://www.discogs.com/oauth/authorize'
    ACCESS_TOKEN_URL = 'http://api.discogs.com/oauth/access_token'

    def __init__(self, consumer_key, consumer_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.client = OAuth1Session(consumer_key, client_secret=consumer_secret)

    def _parse_headers(self, headers):
        return dict([i.strip().split('=') for i in
                     headers['Authorization'].split(',')])

    def request_token(self):
        response = self.client.get(self.REQUEST_TOKEN_URL)
        data = dict(urllib2.urlparse.parse_qsl(response.content))
        self.client = OAuth1Session(self.consumer_key,
                                    client_secret=self.consumer_secret,
                                    resource_owner_key=data['oauth_token'],
                                    resource_owner_secret=data['oauth_token_secret'])
        response = self.client.get(self.AUTHORIZE_URL)



