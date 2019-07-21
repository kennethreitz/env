#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test env module."""

import env
import os
import mock

try:
    from urlparse import urlparse as _urlparse
except ImportError:
    from urllib.parse import urlparse as _urlparse

SEARCH_PREFIX = 'env1'
MATCH_DATA = {'env1TESTS1': 'aA', 'ENV1tests2': 'bB', 'env1tests3': 'cC'}
NO_MATCH_DATA = {'env2TESTS4': 'dD', 'ENV2tests5': 'eE', 'env2tests6': 'fF'}
ALL_DATA = {**MATCH_DATA, **NO_MATCH_DATA}


def test_lower_dict():
    lowereddict = env.lower_dict(MATCH_DATA)

    assert len(lowereddict) == len(MATCH_DATA)

    for item in MATCH_DATA:
        assert MATCH_DATA[item] == lowereddict[item.lower()]


def test_lower_dict_non_string_key():
    mixed_key_dict = {0: 'aA', 'env1TEST1': 'bB'}
    lowereddict = env.lower_dict(mixed_key_dict)
    expected_dict = {0: 'aA', 'env1test1': 'bB'}

    assert len(lowereddict) == len(mixed_key_dict)

    for item in expected_dict:
        assert expected_dict[item] == lowereddict[item]


def test_urlparse():
    urldata = {'url1': 'http://env1.test', 'url2': 'ftp://env2.test'}

    parseddata = env.urlparse(urldata)

    assert len(parseddata) == len(urldata)

    for item in urldata:
        assert _urlparse(urldata[item]) == parseddata[item]


@mock.patch.dict(os.environ, ALL_DATA, clear=True)
def test_prefix():
    prefixsearch = env.prefix(SEARCH_PREFIX)

    assert len(prefixsearch) == len(MATCH_DATA)

    for item in MATCH_DATA:
        assert MATCH_DATA[item] == prefixsearch[item.lower()[len(SEARCH_PREFIX):]]


@mock.patch.object(
    env,
    'lower_dict',
    return_value={0: 'test', 'env1test1': 'bB'}
)
def test_prefix_non_string_key(mock_func):
    prefixsearch = env.prefix(SEARCH_PREFIX)

    assert len(prefixsearch) == 1
    assert prefixsearch['test1'] == 'bB'


@mock.patch.dict(os.environ, ALL_DATA, clear=True)
def test_map():
    mapdata = {'a': 'env1tests1', 'b': 'env1tests2', 'c': 'env1tests3'}
    originaldata = {'env1tests1': 'aA', 'env1tests2': 'bB', 'env1tests3': 'cC'}

    mapsearch = env.map(a='env1tests1', b='env1tests2', c='env1tests3')

    assert len(mapsearch) == len(mapdata)

    for item in mapdata:
        assert originaldata[mapdata[item]] == mapsearch[item]
