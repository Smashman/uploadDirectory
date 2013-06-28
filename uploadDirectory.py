#!/usr/bin/python -OO
# -*- coding: utf-8 -*-

config = {
	'directory': r'C:\Users\Ben\MvM Bot lines',
	'description': 'Robot-filtered lines from MvM.',
	'license': '{{AudioTF2}}',
	'fileprefix': '',
	'filesuffix': '',
	'username': 'SmashBOT',
	'password': '',
	'wikiURL': 'http://wiki.teamfortress.com/w/api.php'
}

import os
import urllib2
import wikitools

wiki_obj = wikitools.wiki.Wiki(config['wikiURL'])
wiki_obj.login(config['username'], config['password'])
failed = []
classes = ['announcer', 'scout', 'soldier', 'pyro', 'demoman', 'heavy', 'engineer', 'medic', 'sniper', 'spy']
catclasses = {
	'announcer': 'Administrator',
	'scout': 'Scout Robot',
	'soldier': 'Soldier Robot',
	'pyro': 'Pyro Robot',
	'demoman': 'Demoman Robot',
	'heavy': 'Heavy Robot',
	'engineer': 'Engineer Robot',
	'medic': 'Medic Robot',
	'sniper': 'Sniper Robot',
	'spy': 'Spy Robot'
}
files = os.listdir(config['directory'])
files.sort()
try:
	for f in files:
		i = f.rfind('.')
		if i == -1:
			continue
		print 'Uploading', config['directory'] + os.sep + f, 'as', config['fileprefix'] + f[:i] + config['filesuffix'] + f[i:], '...'
		category = ''
		smallest = 99999999
		for c in classes:
			if f.find(c) != -1 and f.find(c) < smallest:
				smallest = f.find(c)
				category = '\n[[Category:'+catclasses[c]+' audio responses]]'
		if True:
			file_obj = wikitools.wikifile.File(wiki_obj,"File:"+config['fileprefix'] + f[:i] + config['filesuffix'] + f[i:])
			file_obj.upload(open(config['directory'] + os.sep + f, "rb"),config['description'] +"\n"+ config['license'] + category,ignorewarnings=True)
		else:
			print 'Failed', f
			failed.append(f)
except KeyboardInterrupt:
	print 'Stopped.'
print 'Failed:', failed
