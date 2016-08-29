# -*- coding: utf-8 -*-

import urllib2

import settings
from settings import cli_log as log
from cli.parser import YAMLParser

import logging


class RequestProxy(object):
	"""docstring for RequestProxy"""
	def __init__(self, host):
		super(RequestProxy, self).__init__()
		self.host = host

	def push_task(self, recipe):
		if recipe.endswith('yaml'):
			recipe_as_json = YAMLParser().read(recipe)

		req = urllib2.Request(url=self.host+settings.CHIME_SERVER_ROUTER["tasks"],
							  data=recipe_as_json)
		
		log.info("push task {brief}... to host {host}".format(
			brief=recipe_as_json[:20], 
			host=self.host))
		
		resp = urllib2.urlopen(req).read()
		log.info("received response: {resp}".format(resp=resp))
		