from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.0.1'
DESCRIPTION = ' This simple script sorts all the words in the text by popularity in descending order '
LONG_DESCRIPTION = ' This simple script sorts all the words in the text by popularity in descending order '

# Setting up
setup(
    name="textsorter",
    version=VERSION,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['textsorter'],
)