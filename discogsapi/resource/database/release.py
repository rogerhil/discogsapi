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

""" Module for Discogs Releases resources.
"""

from discogsapi.resource.base import Resource
from discogsapi.resource.entity import EntityResource, EntityResourceGenerator
from discogsapi.category.categories import Database


class Release(EntityResource):
    """ This class wraps a Release details coming from Discogs API

    >>> from discogs import Discogs
    >>> discogs = Discogs("HeyBaldock/1.0 +http://heybaldock.com.br")
    >>> releases_resource = ReleasesResource(discogs)
    >>> release = Release(releases_resource, 45)
    >>> release
    <Release: Push Along EP>
    """

    def __unicode__(self):
        return u'Release: %s' % self.title


class Releases(EntityResourceGenerator):
    """ This is a generator class for Release entities items.

    >>> from discogs import Discogs
    >>> from resource.database.artist import ArtistsResource
    >>> discogs = Discogs("HeyBaldock/1.0 +http://heybaldock.com.br")
    >>> artists_resource = ArtistsResource(discogs)
    >>> releases = Releases(artists_resource, 45, 'releases')
    >>> releases
    <__main__.Releases Generator: [<Release: Analog Bubblebath Vol 2>, <Release: Analogue Bubblebath>, <Release: Digeridoo>, '...']>
    """
    item_class = Release


class ReleasesResource(Resource):
    """ Class for the Releases resources
    """
    name = "releases"
    category = Database

    def __unicode__(self):
        return u'<Releases Resource>'

    def get(self, id):
        """ Returns the Release details as a Release entity.

        >>> from discogs import Discogs
        >>> discogs = Discogs("HeyBaldock/1.0 +http://heybaldock.com.br")
        >>> releases_resource = ReleasesResource(discogs)
        >>> releases_resource.get(45)
        <Release: Push Along EP>
        """
        return Release(self, id)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
