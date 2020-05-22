#!/usr/bin/env python

from io import open
from os import path
from setuptools import find_packages, setup

# Package meta-data.
NAME = 'extsum'
DESCRIPTION = 'Extract ID from Picsum photos'
URL = 'https://github.com/streof/extsum'
REQUIRES_PYTHON = '>=3.8, <4'
VERSION = '0.1.0'

REQUIRED = [
    'requests>=2.23.0,<3',
]

TESTS_REQUIRED = [
    'pytest>=5.4.2',
]

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
try:
    with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(path.join(here, project_slug, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION


setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(),
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    keywords='exif metadata picsum jpeg',

    entry_points={
        'console_scripts': [
            'extsum=extsum.__main__',
        ],
    },

    extras_require={
        "dev": TESTS_REQUIRED
    },
)

