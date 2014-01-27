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

""" Module for Entity classes for resources.
    Each item from Discogs resources is wrapped into a EntityResource object.
"""

class EntityResourceException(Exception):
    pass


class EntityResource(object):
    """ Base class for EntityResource.
    Each item from Discogs resources is wrapped into a EntityResource object.

    >>> from discogs import Discogs
    >>> from category.categories import Database
    >>> from resource.database.artist import Resource
    >>> discogs = Discogs("HeyBaldock/1.0 +http://heybaldock.com.br")
    >>> resource = Resource(discogs)
    >>> resource.name = 'artists'
    >>> resource.category = Database
    >>> entity = EntityResource(resource, '45')
    >>> entity
    <EntityResource: artists>
    >>> getattr(entity, 'name', None)
    'Aphex Twin'
    """

    def __init__(self, resource, id=None, subpath='',data=None):
        self.resource = resource
        if not data:
            subpath = "/%s" % subpath if subpath else ''
            data = self.resource.get_data('%s%s' % (id, subpath))
        for key, value in data.items():
            setattr(self, key, value)

    def __unicode__(self):
        return u'EntityResource: %s' % self.resource.name

    def __str__(self):
        return self.__unicode__().encode('utf-8')

    def __repr__(self):
        return "<%s>" % self.__str__()


class EntityResourceGeneratorPagination(EntityResource):
    """ Base class for a paginator of a EntityResourceGenerator.
    A list of EntityResources may have pages, and this class has the correspond
    properties of a paginator such as:
        page: the page number,
        pages: total number of pages,
        items: total items,
        per_page: number of items per page (default is 50)
        urls: a dict containing the following keys and values:
            first: api url for the first page
            prev: api url for the previous page
            next: api url for the next page
            last: api url for the last page

    >>> from discogs import Discogs
    >>> from category.categories import Database
    >>> from resource.database.artist import Resource
    >>> discogs = Discogs("HeyBaldock/1.0 +http://heybaldock.com.br")
    >>> resource = Resource(discogs)
    >>> resource.name = 'artists'
    >>> resource.category = Database
    >>> releases = EntityResource(resource, '45/releases')
    >>> isinstance(releases.pagination, dict)
    True
    >>> releases.pagination.has_key('per_page')
    True
    >>> releases.pagination['per_page']
    50
    >>> p = EntityResourceGeneratorPagination(resource, data=releases.pagination)
    >>> p.page
    1
    >>> p.pages > 1
    True
    >>> p.per_page
    50
    >>> p.items >= (p.pages - 1) * p.per_page
    True
    >>> isinstance(p.urls, dict)
    True
    >>> p.urls.has_key('next')
    True
    >>> p.urls.has_key('last')
    True
    >>> p.urls['next'].startswith('http')
    True
    >>> p.urls['last'].startswith('http')
    True
    """
    def __unicode__(self):
        return u'Page %s of %s with %s items per page. Total: %s' % (self.page,
                                         self.pages, self.per_page, self.items)


class EntityResourceGenerator:
    """ A generator for a list of resources.
    Since a list of resources may be paginated, this generator will call the
    next page only if needed.
    """
    item_class = None

    def __init__(self, resource, id, key_list=None):
        self.resource = resource
        self.key_list = key_list
        self.index = 0
        self.entities = []
        if not self.item_class:
            raise EntityResourceException('item_class must be set in the '
                                          'subclass of and EntityResource')
        data = self.resource.get_data("%s/%s" % (id, key_list))
        self._set_data(data)

    def __unicode__(self):
        entities = self.entities[:3] + ['...']
        return u'%s Generator: %s' % (self.__class__, entities)

    def __str__(self):
        return self.__unicode__().encode('utf-8')

    def __repr__(self):
        return "<%s>" % self.__str__()

    def __iter__(self):
        """ This classifies this class as an iterator.
        """
        return self

    def _set_data(self, data):
        """ Receives a dict data previously parsed through a JSON string and
        sets the data and creates a list of EntityResources.
        """
        self.data = data if data else {}
        pag = self.data.get('pagination')
        self.pagination = EntityResourceGeneratorPagination(self.resource,
                                                            data=pag)
        self.data.pop('pagination')
        for key, value in self.data.items():
            setattr(self, key, value)
        alist = self.data.get(self.key_list)
        c = lambda r, d: self.item_class(r, data=d)
        self.entities += [c(self.resource, i) for i in alist]

    def next(self):
        """ This method take care of call the 'next' url of the pagination
        only if reaches the end of the current page.
        """
        if self.index >= len(self.entities):
            next = self.pagination.urls.get('next')
            if not next:
                raise StopIteration
            data = self.resource.discogs.get_data_from_full_url(next)
            self._set_data(data)
        item = self.entities[self.index]
        self.index += 1
        return item


class ImageEntityResource(object):
    """ Base class for an Image EntityResource. It has an attribute for the
    response of the image.
    """

    def __init__(self, resource, filename=None):
        self.resource = resource
        self.filename = filename
        self.response = resource.get_response(filename)

    def __str__(self):
        return self.__unicode__().encode('utf-8')

    def __repr__(self):
        return "<%s>" % self.__str__()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
