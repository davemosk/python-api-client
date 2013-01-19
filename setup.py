#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name='meetup-api',
    version='0.1',
    description='Python interfaces to the Meetup Web API',
    url='https://github.com/dwightgunning/meetup-api',
    long_description=open('README.md', 'r').read(),
    packages=[
        'meetup',
    ],
    requires=[],
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)
