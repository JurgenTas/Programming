"""
:author: juergen.tas@triodos.com

Implements setup.py.
"""
# -*- coding: utf-8 -*-

from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    readme = f.read()

with open(path.join(here, 'LICENSE'), encoding='utf-8') as f:
    license = f.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    required = f.read().splitlines()

setup(
    name='Analytics.AnalyticsLib.Py',
    version='0.1',
    keywords='e-Crime',
    packages=find_packages(exclude=['tests.*', 'test*']),
    include_package_data=True,
    install_requires=required,
    author='Jürgen Tas',
    author_email='juergen.tas@triodos.com',
    description='analytics library',
    long_description=readme,
    license=license
)
