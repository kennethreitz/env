import env, nose
from os import environ
from urlparse import urlparse as _urlparse

searchprefix = 'env1'
matchdata = {'env1TESTS1': 'aA', 'ENV1tests2': 'bB', 'env1tests3': 'cC'}
nomatchdata = {'env2TESTS4': 'dD', 'ENV2tests5': 'eE', 'env2tests6': 'fF'}

for matchvalue in matchdata:
	environ[matchvalue] = matchdata[matchvalue]

for nomatchvalue in nomatchdata:
	environ[nomatchvalue] = nomatchdata[nomatchvalue]

def compare_values(a, b):
	assert a == b

def test_lower_dict():
	lowereddict = env.lower_dict(matchdata)

	yield compare_values, len(lowereddict), len(matchdata)

	for item in matchdata:
		yield compare_values, matchdata[item], lowereddict[item.lower()]

def test_urlparse():
	urldata = {'url1': 'http://env1.test', 'url2': 'ftp://env2.test'}

	parseddata = env.urlparse(urldata)

	yield compare_values, len(parseddata), len(urldata)

	for item in urldata:
		yield compare_values, _urlparse(urldata[item]), parseddata[item]

def test_prefix():
	prefixsearch = env.prefix(searchprefix)

	yield compare_values, len(prefixsearch), len(matchdata)

	for item in matchdata:
		yield compare_values, matchdata[item], prefixsearch[item.lower()[len(searchprefix):]]

def test_map():
	mapdata = {'a': 'env1tests1', 'b': 'env1tests2', 'c': 'env1tests3'}
	originaldata = {'env1tests1': 'aA', 'env1tests2': 'bB', 'env1tests3': 'cC'}

	mapsearch = env.map(a='env1tests1', b='env1tests2', c='env1tests3')

	yield compare_values, len(mapsearch), len(mapdata)

	for item in mapdata:
		yield compare_values, originaldata[mapdata[item]], mapsearch[item]
