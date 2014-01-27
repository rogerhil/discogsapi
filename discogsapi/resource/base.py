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

""" Base module for all resources coming from Discogs API
"""

from discogsapi.category.base import Category, CategoryException


class ResourceException(Exception):
    pass


class Resource(object):
    """ This is the base class of a Discogs Resource. It requires a Discogs
    instance to create new objects. It has methods to retrieve data information
    from Discogs API.
    Each resource has a 'name' attribute, which means the first item in the
    url path, e.g. Artist.name = 'artists' -> /artists/.
    """
    name = ''
    category = ''

    def __init__(self, discogs):
        self.discogs = discogs
        self.data = {}

    def _get_response_from_resource(self, subpath, params=None):
        """ The subpath can be anything after the resource.name.
        e.g. resource=Artist, subpath = 12/releases -> /arttists/12/releases
        It retrieves an addinfourl object response.
        """
        path = "/%s/%s" % (self.name, subpath)
        return self.discogs.get_response(path, params)

    def _get_data_from_resource(self, subpath='', params=None):
        """ The subpath can be anything after the resource.name.
        e.g. resource=Artist, subpath = 12/releases -> /arttists/12/releases
        It returns a dict data, previously parsed from a JSON through the
        Discogs API call.
        """
        category = self.category
        if category not in Category.categories():
            raise CategoryException("There's no category %s" % category)
        subpath = "/%s" % subpath if subpath else ''
        path = "/%s%s" % (self.name, subpath)
        return self.discogs.get_data(path, params)

    def get_data(self, subpath='', params=None):
        """ The subpath can be anything after the resource.name.
        e.g. resource=Artist, subpath = 12/releases -> /arttists/12/releases
        It returns a dict data, previously parsed from a JSON through the
        Discogs API call.

        >>> from discogs import Discogs
        >>> discogs = Discogs("HeyBaldock/1.0 +http://heybaldock.com.br")
        >>> resource = Resource(discogs)
        >>> resource.name = 'artists'
        >>> from category.categories import Database
        >>> resource.category = Database
        >>> data = resource.get_data('45')
        >>> data is not None
        True
        >>> type(data)
        <type 'dict'>
        >>> data.has_key('profile')
        True
        """
        self.data = self._get_data_from_resource(subpath, params)
        return self.data

    def get_response(self, subpath='', params=None):
        """ The subpath can be anything after the resource.name.
        e.g. resource=Artist, subpath = 12/releases -> /arttists/12/releases
        It retrieves an addinfourl object response.

        >>> from discogs import Discogs
        >>> discogs = Discogs("HeyBaldock/1.0 +http://heybaldock.com.br")
        >>> resource = Resource(discogs)
        >>> resource.name = 'artists'
        >>> from category.categories import Database
        >>> resource.category = Database
        >>> response = resource.get_response('45')
        >>> response is not None
        True
        >>> hasattr(response, 'read')
        True
        """
        return self._get_response_from_resource(subpath, params)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
