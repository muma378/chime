import falcon
from http import parser

import settings

api = application = falcon.API()

chime_task = parser.ChimeTask(settings.MESOS_HOST)
api.add_route('/tasks', chime_task)
