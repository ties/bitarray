import os
import uuid

from setuptools import setup

from pip.req import parse_requirements

# noqa from <http://stackoverflow.com/questions/14399534/how-can-i-reference-requirements-txt-for-the-install-requires-kwarg-in-setuptool>
install_reqs = parse_requirements('requirements.txt', session=uuid.uuid1())

reqs = [str(ir.req) for ir in install_reqs]

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="bitarray",
    version="0.0.1",
    author="Ties de Kock",
    author_email="ties@tiesdekock.nl",
    description=("A simple bitarray"),
    license="BSD",
    keywords="bitarray bit manipulation",
    packages=['bitarray'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=reqs
)
