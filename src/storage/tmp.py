# -*- coding: utf-8 -*-


import os

class TemporaryFile(object):
	"""class to manage temporary files, such as pid, info for tasks, """
	def __init__(self, arg):
		super(TemporaryFile, self).__init__()
		self.arg = arg
		