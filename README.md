# DiscogsAPI wrapper for Python

[![Build Status](https://travis-ci.org/rogerhil/discogsapi.png?branch=master)](https://travis-ci.org/rogerhil/discogsapi)

![DiscogsAPI for Python](discogs_logo.png)

This is a Discogs API wrapper for Python. (API version 2.0)


## Usage

    >>> from discogsapi import Discogs
    >>> discogs = Discogs(user_agent="HeyBaldock/1.0 +http://heybaldock.com.br")
    >>> artist = discogs.artists.get(45)
    >>> artist
    <Artist: Aphex Twin>
    >>> artist.name
    'Aphex Twin'

The argument user_agent is required. Discogs API will block ips from requests
with bad user_agent names.
See the advise below from www.discogs.com/developers/accessing.html:
"
Your application must provide a User-Agent string that identifie
itself - preferably something that follows RFC 1945. Some good
examples include:
    AwesomeDiscogsBrowser/0.1 +http://adb.example.com
    LibraryMetadataEnhancer/0.3 +http://example.com/lime
    MyDiscogsClient/1.0 +http://mydiscogsclient.org

Please don't just copy one of those! Make it unique so we can let you
know if your application starts to misbehave - the alternative is that
we just silently block it, which will confuse and infuriate your users.
Here are some bad examples that are unclear or obscure the nature of
the application:
    curl/7.9.8 (i686-pc-linux-gnu) libcurl 7.9.8 (OpenSSL 0.9.6b)
    Mozilla/5.0 (X11; Linux i686; rv:6.0.2) Gecko/20100101 Firefox/6.0
    my app
"

## Resources

Discogs API has many resources in 3 categories:

 * Database
   - Artists
   - Releases
   - Masters
   - Labels
   - Image
   - Search
 * Market Place
   - Fee
   - Inventory
   - Listing
   - Order
   - Price Suggestions
 * User
   - Colletion
   - Identify
   - Profile
   - Wantlist


### Database Category

#### Artists

    >>> from discogsapi import Discogs
    >>> discogs = Discogs(user_agent="HeyBaldock/1.0 +http://heybaldock.com.br")
    >>> artist = discogs.artists.get(45)
    >>> artist
    <Artist: Aphex Twin>
    >>> artist.name
    'Aphex Twin'
    >>> releases = artist.releases()
    >>> releases
    <discogsapi.resource.database.release.Releases Generator: [<Release: Analog Bubblebath Vol 2>, <Release: Analogue Bubblebath>, <Release: Digeridoo>, '...']>
    >>> releases.next()
    <Release: Analog Bubblebath Vol 2>
    >>> releases.next()
    <Release: Analogue Bubblebath>

Possible Artist attributes:
 * images
 * members
 * name
 * namevariations
 * realname
 * urls
 * releases -> will retrieve a generator with Release instances


#### Releases

The Discogs.releases resource retrieves a generator with Release instances,
see below:

    >>> from discogs import Discogs
    >>> from resource.database.artist import ArtistsResource
    >>> discogs = Discogs("HeyBaldock/1.0 +http://heybaldock.com.br")
    >>> releases = discogs.releases.get(45)
    >>> releases
    <Release: Push Along EP>


#### Masters
The Discogs.masters resource retrieves a Master instance with the correspond
details:

    >>> discogs = Discogs("HeyBaldock/1.0 +http://heybaldock.com.br")
    >>> discogs.masters.get(8471)
    <Master: Back In Black>

#### Labels
The Discogs.masters resource retrieves a Master instance with the correspond
details:

    >>> discogs = Discogs("HeyBaldock/1.0 +http://heybaldock.com.br")
    >>> discogs.labels.get(45)
    <Label: Groovin' Records>


#### Image

The Discogs.images resource provides an Image instance with the response
image data:

    >>> discogs = Discogs("HeyBaldock/1.0 +http://heybaldock.com.br")
    >>> image = discogs.images.get('R-150-63114-1148806222.jpeg')
    >>> image
    <Image: R-150-63114-1148806222.jpeg>
    >>> getattr(image, 'response', None) is not None
    True


#### Search

The Discogs.search resource provides a query search:

    >>> discogs = Discogs("HeyBaldock/1.0 +http://heybaldock.com.br")
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

