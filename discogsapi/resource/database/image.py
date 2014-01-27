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

""" Module for Discogs Images Resources
"""

from discogsapi.resource.base import Resource
from discogsapi.resource.entity import ImageEntityResource
from discogsapi.category.categories import Database


class Image(ImageEntityResource):
    """ Class for the Image Entity Resource
    >>> from discogs import Discogs
    >>> discogs = Discogs("HeyBaldock/1.0 +http://heybaldock.com.br")
    >>> image_resource = ImageResource(discogs)
    >>> image = Image(image_resource, 'R-150-63114-1148806222.jpeg')
    >>> image
    <Image: R-150-63114-1148806222.jpeg>
    >>> getattr(image, 'response', None) is not None
    True
    """

    def __unicode__(self):
        return u'Image: %s' % self.filename


class ImageResource(Resource):
    """ Class for the Images resources
    """
    name = "image"
    category = Database

    def __unicode__(self):
        return u'<Image Resource>'

    def get(self, filename):
        """ Returns a Image based on ImageEntityResource with the response
        containg the image data.
        >>> from discogs import Discogs
        >>> discogs = Discogs("HeyBaldock/1.0 +http://heybaldock.com.br")
        >>> image_resource = ImageResource(discogs)
        >>> image = image_resource.get('R-150-63114-1148806222.jpeg')
        >>> image
        <Image: R-150-63114-1148806222.jpeg>
        >>> getattr(image, 'response', None) is not None
        True
        """
        return Image(self, filename)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
