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

""" Module for the Discogs Search resource.
"""

from discogsapi.resource.base import Resource
from discogsapi.category.categories import Database


class SearchResource(Resource):
    """ Class for the Search resource
    """
    name = "search"
    category = Database

    def __unicode__(self):
        return u'<Image Resource>'

    def query(self, params):
        """ Returns details of a search through the queries params

        >>> from discogs import Discogs
        >>> discogs = Discogs("HeyBaldock/1.0 +http://heybaldock.com.br")
        >>> search_resource = SearchResource(discogs)
        >>> results = search_resource.query(dict(q='The Beatles',
        ...                                      type='artist'))
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
        return self.get_data(params=params)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
