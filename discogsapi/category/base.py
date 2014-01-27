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


class CategoryException(Exception):
    pass


class CategoryMetaclass(type):
    def __new__(cls, name, bases, dct):
        new_attrs = {}
        for attr, value in dct.items():
            if attr.startswith('__'):
                new_attrs[attr] = value
                continue
        def categories():
            import categories
            g = lambda x: getattr(categories, x)
            return [g(i) for i in dir(categories) if isinstance(g(i),
                                                                Category)]
        new_attrs['categories'] = staticmethod(categories)
        new_class = super(CategoryMetaclass, cls).__new__(cls, name, bases,
                                                          new_attrs)
        if name == 'Category':
            return new_class
        else:
            return new_class(dct['name'])


class Category(str):
    """ Category base class
    """
    __metaclass__ = CategoryMetaclass
    name = ''
    resources = []

