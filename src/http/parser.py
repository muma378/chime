
import os
import json
import falcon

from settings import log
import settings

class ChimeTask(object):
	def __init__(self, master):
		self.master = master

	def on_post(self, req, resp):
		log.info("received a request from {ip} for establishing tasks".format(ip=req.remote_addr))
		recipe = ""
		while True:
			chunk = req.sitream.read(settings.CHUNK_SIZE)
			if not chunk:
				break

			log.info("size of chunk received is {chunk_size}".format(chunk_size=len(chunk)))
			recipe += chunk
		
		task = json.loads(recipe)
		task_info = TaskBuilder(task).build()


	def on_get(self, req, resp):
		import pdb;pdb.set_trace()