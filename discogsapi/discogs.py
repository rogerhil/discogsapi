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

""" Main module of Discogs API Python Wrapper.
"""

from discogsapi.base import DiscogsBase
from discogsapi.resource.database.artist import ArtistsResource
from discogsapi.resource.database.master import MastersResource
from discogsapi.resource.database.label import LabelsResource
from discogsapi.resource.database.release import ReleasesResource
from discogsapi.resource.database.image import ImageResource
from discogsapi.resource.database.search import SearchResource


class Discogs(DiscogsBase):
    """ Main class of Discogs API Python Wrapper. It contains the following
    resources:
      - artists:
            get(id): get an artist details, an Artist EntityResource
            get_releases(id): get an artist's releases, an
                          EntityResourceGenerator with Releases EntityResources
      - releases:
            get(id): get a release details, a Release EntityResource
      - masters:
            get(id): get a master release, a Release EntityResource
      - labels:
            get(id): get a label details, a Label EntityResource
      - images:
            get(filename): get an image, an addinfourl object response
      - search:
            query(params): run a search query

    >>> discogs = Discogs("HeyBaldock/1.0 +http://heybaldock.com.br")
    >>> discogs.artists.get(45)
    <Artist: Aphex Twin>
    >>> discogs.releases.get(45)
    <Release: Push Along EP>
    >>> discogs.masters.get(8471)
    <Master: Back In Black>
    >>> discogs.labels.get(45)
    <Label: Groovin' Records>
    >>> image = discogs.images.get('R-150-63114-1148806222.jpeg')
    >>> image
    <Image: R-150-63114-1148806222.jpeg>
    >>> getattr(image, 'response', None) is not None
    True
    >>> results = discogs.search.query(dict(q='The Beatles', type='artist'))
    >>> isinstance(results, dict)
    True
    >>> results.has_key('resp')
    True
    >>> results['resp'].has_key('status')
    True
    >>> results['resp'].has_key('search')
    True
    >>> results['resp']['search'].has_key('searchresults')
    True
    >>> results['resp']['search']['searchresults'].has_key('numResults')
    True
    >>> results['resp']['search']['searchresults']['numResults'].isdigit()
    True
    >>> int(results['resp']['search']['searchresults']['numResults']) > 0
    True
    """

    def __init__(self, *args, **kwargs):
        super(Discogs, self).__init__(*args, **kwargs)
        self.artists = ArtistsResource(self)
        self.releases = ReleasesResource(self)
        self.masters = MastersResource(self)
        self.labels = LabelsResource(self)
        self.images = ImageResource(self)
        self.search = SearchResource(self)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
