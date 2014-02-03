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

""" Module for Discogs Labels Resources
"""

from discogsapi.resource.base import Resource
from discogsapi.resource.entity import EntityResource
from discogsapi.category.categories import Database


class Label(EntityResource):
    """ This class wraps the Label details coming from Discogs API

    >>> from discogsapi import Discogs
    >>> discogs = Discogs("HeyBaldock/1.0 +http://heybaldock.com.br")
    >>> labels_resource = LabelsResource(discogs)
    >>> data = labels_resource.get_data(45)
    >>> label = Label(labels_resource, data)
    >>> label
    <Label: Groovin' Records>
    """

    def __unicode__(self):
        return u'Label: %s' % self.name


class LabelsResource(Resource):
    """ Class for the Labels resources
    """
    name = "labels"
    category = Database

    def __unicode__(self):
        return u'<Labels Resource>'

    def get(self, id):
        """ Returns the Label details, a Label EntityResource.

        >>> from discogsapi import Discogs
        >>> discogs = Discogs("HeyBaldock/1.0 +http://heybaldock.com.br")
        >>> labels_resource = LabelsResource(discogs)
        >>> labels_resource.get(45)
        <Label: Groovin' Records>
        """
        data = self.get_data(45)
        return Label(self, data)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
