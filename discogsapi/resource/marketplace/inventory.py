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

""" Module for Discogs Inventories Resources
"""

from discogsapi.resource.entity import EntityResource, EntityResourceGenerator


class InventoryListing(EntityResource):
    """ This class wraps an Inventory Listing details
    """
    def __unicode__(self):
        return u'Listing: %s' % self.status


class InventoryListings(EntityResourceGenerator):
    """ This is a generator class for Inventory Listings entities items for a
    given user Inventory.

    >>> from discogsapi import Discogs
    >>> from discogsapi.resource.user.resources import UsersResource
    >>> discogs = Discogs("HeyBaldock/1.0 +http://heybaldock.com.br")
    >>> users_resource = UsersResource(discogs)
    >>> inventory = users_resource.get_inventory_listings('paul')
    >>> inventory
    <InventoryListings Generator: ['...']>
    """
    item_class = InventoryListing


if __name__ == "__main__":
    import doctest
    doctest.testmod()
