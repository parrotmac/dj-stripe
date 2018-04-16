#!/usr/bin/env python
from __future__ import absolute_import, division, print_function, unicode_literals

import os
import sys

from setuptools import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py bdist_wheel upload --sign')
    sys.exit()


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')


setup(
    name='dj-stripe',
    version='2.0.0.a0',
    packages=[
        'djstripe',
    ],
    package_dir={'djstripe': 'djstripe'},
    include_package_data=True,
    long_description=readme + '\n\n' + history,
)
