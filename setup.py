# -*- coding: utf-8 -*-
"""
env.py
~~~~~~

Mapping environment variables can be a bit of a pain.

Now you can replace this boilerplate::

    ZENDESK_URL = os.environ['ZENDESK_URL']
    ZENDESK_USER = os.environ['ZENDESK_USER']
    ZENDESK_PASS = os.environ['ZENDESK_PASS']
    ZENDESK_VIEW = os.environ['ZENDESK_VIEW']

With a simple call::

    import env

::

    >>> zendesk = env.prefix('zendesk_')
    >>> zendesk
    {'user': ..., 'pass': ..., 'url': ..., 'view': ...}

Or have a bit more control::

    >>> env.map(user='zendesk_user')
    {'user': ...}


"""

from setuptools import setup

setup(
    name='env',
    version='0.1.1',
    url='https://github.com/kennethreitz/env',
    license='BSD',
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    description='Environment Variables for Humans',
    long_description=__doc__,
    py_modules=['env'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
