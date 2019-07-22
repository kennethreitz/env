Env: Environment Variables for Humans
=====================================

.. image:: https://travis-ci.org/MasterOdin/env.svg?branch=master
    :target: https://travis-ci.org/MasterOdin/env
    :alt: Build Status
.. image:: https://coveralls.io/repos/github/MasterOdin/env/badge.svg?branch=master
    :target: https://coveralls.io/github/MasterOdin/env?branch=master
    :alt: Coverage Status

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


Installation
------------

Installation is easy with pip::

    $ pip install env
