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

""" Module for Discogs Market Place Listings
"""

from discogsapi.category import categories
from discogsapi.resource.base import Resource
from discogsapi.resource.marketplace.inventory import InventoryListing


class InventoryListingResource(Resource):
    """ This class wraps a Market Place Listing resource
    """
    category = categories.MarketPlace
    name = 'marketplace'

    def get(self, id):
        """ Gets the Inventory Resource details by id

        >>> from discogsapi import Discogs
        >>> from discogsapi.resource.user.resources import UsersResource
        >>> discogs = Discogs("HeyBaldock/1.0 +http://heybaldock.com.br")
        >>> resource = InventoryListingResource(discogs)
        >>> listing = resource.get('41578240')
        

        """
        data = self.get_data(('listings', id))
        return InventoryListing(self, data)


if __name__ == "__main__":
    import doctest
    doctest.testmod()