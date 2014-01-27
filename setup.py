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
