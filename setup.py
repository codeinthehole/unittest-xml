#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='unittest-xml',
      version='0.2.1',
      url='https://github.com/codeinthehole/unittest-xml',
      author="David Winterbottom",
      author_email="david.winterbottom@tangentlabs.co.uk",
      description="Additional assertion methods for testing XML",
      long_description=open('README.rst').read(),
      keywords="XML, testing",
      platforms=['linux'],
      packages=find_packages(exclude=['tests']),
      install_requires=['unittest',],
      )
