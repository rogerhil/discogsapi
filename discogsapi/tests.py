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

import doctest
from unittest import TestCase

from discogsapi.discogs import Discogs
from discogsapi.resource.database.artist import Artist

doctest.testfile('../README.md', optionflags=doctest.ELLIPSIS)


class DatabaseTestCase(TestCase):

    def setUp(self):
        self.discogs = Discogs("HeyBaldock/1.0 +http://heybaldock.com.br")

    def test_artists(self):
        artist = self.discogs.artists.get(45)
        self.assertIsNotNone(artist)
        self.assertIsInstance(artist, Artist)
        self.assertTrue(hasattr(artist, 'name'))
        self.assertEquals(artist.name, 'Aphex Twin')

        releases = self.discogs.artists.get_releases(45)
        self.assertIsNotNone(releases)
        self.assertTrue(hasattr(releases, 'next'))
        self.assertTrue(hasattr(releases.next, '__call__'))
        release = releases.next()
        self.assertIsNotNone(release)
        self.assertTrue(hasattr(release, 'title'))


if __name__ == "__main__":
    from unittest import main
    main()