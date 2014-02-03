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

""" Module for Discogs Masters Resources
"""

from discogsapi.resource.base import Resource
from discogsapi.resource.entity import EntityResource
from discogsapi.category.categories import Database


class Master(EntityResource):
    """ This class wraps a Master details coming from Discogs API
        >>> from discogsapi import Discogs
        >>> discogs = Discogs("HeyBaldock/1.0 +http://heybaldock.com.br")
        >>> masters_resource = MastersResource(discogs)
        >>> data = masters_resource.get_data(8471)
        >>> master = Master(masters_resource, data)
        >>> master
        <Master: Back In Black>
    """

    def __unicode__(self):
        return u'Master: %s' % self.title


class MastersResource(Resource):
    """ Class for the Masters resources
    """
    name = "masters"
    category = Database

    def __unicode__(self):
        return u'<Masters Resource>'

    def get(self, id):
        """ Returns the Master details, a Master EntityResource.

        >>> from discogsapi import Discogs
        >>> discogs = Discogs("HeyBaldock/1.0 +http://heybaldock.com.br")
        >>> masters_resource = MastersResource(discogs)
        >>> masters_resource.get(8471)
        <Master: Back In Black>
        """
        data = self.get_data(8471)
        return Master(self, data)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
