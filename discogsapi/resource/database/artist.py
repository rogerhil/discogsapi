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

""" Module for Discogs Artists Resources
"""

from discogsapi.resource.base import Resource
from discogsapi.resource.entity import EntityResource
from discogsapi.category.categories import Database
from discogsapi.resource.database.release import Releases


class Artist(EntityResource):
    """ This class wraps an Artist details coming from Discogs API
    """

    def __unicode__(self):
        return u'Artist: %s' % self.name

    def releases(self):
        """ Retrieves an EntityResourceGenerator containing the artist's
        releases, wrapped as Artist EntityResource.
        NOTE: This method returns just the result of get_releases method of
        the ArtistsResource class.

        >>> from discogs import Discogs
        >>> discogs = Discogs("HeyBaldock/1.0 +http://heybaldock.com.br")
        >>> artists_resource = ArtistsResource(discogs)
        >>> artist = Artist(artists_resource, 45)
        >>> artist.releases()
        <release.Releases Generator: [<Release: Analog Bubblebath Vol 2>, <Release: Analogue Bubblebath>, <Release: Digeridoo>, '...']>
        """
        return ArtistsResource(self.resource.discogs).get_releases(self.id)


class ArtistsResource(Resource):
    """ Class for the Artists resources
    """
    name = "artists"
    category = Database

    def __unicode__(self):
        return u'<Artists Resource>'

    def get(self, id):
        """ Returns an artist details, an Artist EntityResource.

        >>> from discogs import Discogs
        >>> discogs = Discogs("HeyBaldock/1.0 +http://heybaldock.com.br")
        >>> artists_resource = ArtistsResource(discogs)
        >>> artist = artists_resource.get(45)
        >>> artist
        <Artist: Aphex Twin>
        >>> artist.namevariations
        ['A-F-X Twin', 'A.F.X.', 'A.Twin', 'AFX', 'Apex Twin', 'Aphex Twin, The', 'Aphex Twins', 'TheAphexTwin']
        """
        return Artist(self, id)

    def get_releases(self, id):
        """ Returns artist's releases, an EntityResourceGenerator with Releases
        EntityResources.

        >>> from discogs import Discogs
        >>> discogs = Discogs("HeyBaldock/1.0 +http://heybaldock.com.br")
        >>> artists_resource = ArtistsResource(discogs)
        >>> artists_resource.get_releases(45)
        <release.Releases Generator: [<Release: Analog Bubblebath Vol 2>, <Release: Analogue Bubblebath>, <Release: Digeridoo>, '...']>
        """
        return Releases(self, id, "releases")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
