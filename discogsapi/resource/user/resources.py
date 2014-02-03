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

from discogsapi.category import  categories
from discogsapi.resource.base import Resource
from discogsapi.resource.entity import EntityResource
from discogsapi.resource.marketplace.inventory import InventoryListings


class User(EntityResource):
    """ This class wraps an User details
    """

    def __unicode__(self):
        return u'User: %s' % self.username

    def inventory_listings(self):
        """ Retrieves an EntityResourceGenerator containing the user's
        details.

        >>> from discogsapi import Discogs
        >>> discogs = Discogs("HeyBaldock/1.0 +http://heybaldock.com.br")
        >>> users_resource = UsersResource(discogs)
        >>> data = users_resource.get_data('example')
        >>> isinstance(data, dict)
        True
        >>> data.get('username')
        'example'
        >>> data.get('id')
        1991843
        >>> user = User(users_resource, data)
        >>> user
        <User: example>
        >>> user.username
        'example'
        """
        users_resources = UsersResource(self.resource.discogs)
        return users_resources.get_inventory_listings(self.username)


class UsersResource(Resource):
    """ Class for the Users resources
    """
    name = "users"
    category = categories.User

    def __unicode__(self):
        return u'<Users Resource>'

    def get(self, username):
        """ Returns an artist details, an Artist EntityResource.

        >>> from discogsapi import Discogs
        >>> discogs = Discogs("HeyBaldock/1.0 +http://heybaldock.com.br")
        >>> users_resource = UsersResource(discogs)
        >>> user = users_resource.get('example')
        >>> user
        <User: example>
        >>> user.username
        'example'
        """
        data = self.get_data(username)
        return User(self, data)

    def get_inventory_listings(self, username):
        """ Returns artist's releases, an EntityResourceGenerator with Releases
        EntityResources.

        >>> from discogsapi import Discogs
        >>> discogs = Discogs("HeyBaldock/1.0 +http://heybaldock.com.br")
        >>> users_resource = UsersResource(discogs)
        >>> users_resource.get_inventory_listings('example')
        <InventoryListings Generator: ['...']>
        """
        return InventoryListings(self, username, 'listings', 'inventory')


if __name__ == "__main__":
    import doctest
    doctest.testmod()