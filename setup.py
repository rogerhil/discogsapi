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

import os
from setuptools import setup, find_packages

local_file = lambda f: open(os.path.join(os.path.dirname(__file__), f)).read()

if __name__ == '__main__':
    setup(
        name='discogsapi',
        version='0.0.1',
        description='Discogs API for python. API version 2.0.',
        long_description=local_file('README.md'),
        author='Rogerio Hilbert Lima',
        author_email='rogerhil@gmail.com',
        url='https://github.com/rogerhil/discogsapi',
        packages=find_packages(exclude=['*tests*'])
    )
