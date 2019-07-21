# -*- coding: utf-8 -*-
"""Parses env variables into a human friendly dictionary."""

from os import environ
try:  # pragma: no cover
    from urllib.parse import urlparse as _urlparse
except ImportError:  # pragma: no cover
    from urlparse import urlparse as _urlparse


def lower_dict(d):
    """Lower cases string keys in given dict."""
    _d = {}

    for k, v in d.items():
        try:
            _d[k.lower()] = v
        except AttributeError:
            _d[k] = v

    return _d


def urlparse(d, keys=None):
    """Return a copy of the given dictionary with url values parsed."""
    d = d.copy()

    if keys is None:
        keys = d.keys()

    for key in keys:
        d[key] = _urlparse(d[key])

    return d


def prefix(prefix):
    """
    Return dictionary with all environment variables starting with prefix.

    The elements of the dictionary are all lower cased and stripped of prefix.
    """
    d = {}
    e = lower_dict(environ.copy())

    prefix = prefix.lower()

    for k, v in e.items():
        try:
            if k.startswith(prefix):
                k = k[len(prefix):]
                d[k] = v
        except AttributeError:
            pass

    return d


def map(**kwargs):
    """
    Return a dictionary of the given keyword arguments mapped to os.environ.

    The input keys are lower cased for both the passed in map and os.environ.
    """
    d = {}
    e = lower_dict(environ.copy())

    for k, v in kwargs.items():
        d[k] = e.get(v.lower())

    return d
