# -*- coding: utf-8 -*-
"""
Setup file for env package.

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
from setuptools.command.test import test as TestCommand
import sys


class PyTest(TestCommand):
    """pytest command runner."""

    user_options = [('pytest-args=', 'a', "Arguments to pass into py.test")]

    def initialize_options(self):
        """Initialize the options for pytest."""
        TestCommand.initialize_options(self)

    def finalize_options(self):
        """Finalize the options for pytest."""
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        """Run the pytest runner."""
        import pytest

        errno = pytest.main([])
        sys.exit(errno)


setup(
    name='env',
    version='0.1.1',
    url='https://github.com/MasterOdin/env',
    license='BSD',
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    description='Environment Variables for Humans',
    long_description=__doc__,
    py_modules=['env'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    tests_require=['pytest', 'pytest-cov'],
    cmdclass={'test': PyTest},
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
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
