import os

from setuptools import setup, find_packages

REQUIREMENTS = []


def read(fname):
    """ Utility function to read the README file.
    Used for the long_description.  It's nice, because now (1) we have a top
    level README file and (2) it's easier to type in the README file than to
    put a raw string in below ...
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="bitarray",
    version="0.0.1",
    author="Ties de Kock",
    author_email="ties@tiesdekock.nl",
    description=("A simple bitarray"),
    license="MIT",
    keywords="bitarray bit manipulation",
    packages=find_packages(exclude=['examples', 'tests', 'tests.*']),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=REQUIREMENTS
)
