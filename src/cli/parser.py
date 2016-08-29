import os
import sys
import json
import yaml
import logging

from settings import cli_log as log



class YAMLParser(object):
	"""
	it receives a template to indicate the required and optional params and types
	then reads files, whic are ought to be yaml,  and checks their availability to ensure
	only params listed above was included
	"""
	def __init__(self, template=None):
		super(YAMLParser, self).__init__()
		if template:
			if not os.path.isfile(template):
				err_msg = "initialize failed, cause template {name} is not found".format(name=template)
				log.error(err_msg)
				raise IOError(err_msg)
			else:
				log.info("template {name} is initialized for YAMLParser".format(name=template))
				self.template = yaml.load(file(template, 'r'))
		else:
			self.template = None

	def read(self, filename):
		if not os.path.isfile(filename):
			err_msg = "{filename} does not exist".format(filename=filename)
			log.error(err_msg)
			raise IOError(err_msg)
		else:
			recipe = yaml.load(file(filename, 'r'))
			log.info("{filename} is loaded as yaml".format(filename=filename))
			if self.check(recipe, self.template):
				return json.dumps(recipe)				

	# TODO: check its availability
	def check(self, recipe, template):
		if template:
			for key, val in recipe.items():
				if template.get(key):
					spec_type = template[key]
					if isinstance(spec_type, list):
						if isinstance(val, list):
							log.error("value for key {key} is ought to be a list".format(key=key))
							return False
						for sub_element in val:
							if not self.check(sub_element, spec_type[0]):
								return False
					elif spec_type is not "str": 
						if repr(val).find(spec_type) == -1:
							log.error("keys {key} in recipe and template are not matched".format(key=key))
							return False
					else:
						# converting to a specific type
						pass
					
				else:
					log.error("key {key} does not exist in template".format(key=key))
					return False

		return True