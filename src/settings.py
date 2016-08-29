# -*- coding: utf-8 -*-
# defined by developers, basically settings are for the system
# rarely needed to be modified

import os
import logging
import logging.config

# PROJECT_ROOT = os.path.dirname(__file__)
PROJECT_ROOT = os.getcwd()
LOGGING_CONF_FILE = '%(PROJECT_ROOT)s/conf/logging.conf' % locals() 


logging.config.fileConfig(LOGGING_CONF_FILE)
log = logging.getLogger('root')

cli_log = logging.getLogger('cli')


CHIME_SERVER_ROUTER = {
	"tasks": "/tasks",
}


CHIME_TASK_PATH = "/tmp/chime/{username}/{taskname}"
# settins for executors in chime
CHIME_TASK_COMMON_NAME = "chime-task"
CHIME_EXECUTOR_ID = "chime-executor"
CHIME_EXECUTOR_COMMAND = "bin/start chime slave"

CHIME_RESOURCE_CPUS = "cpus"
CHIME_RESOURCE_MEM 	= "mem"
CHIME_RESOURCE_PORT = "port"
CHIME_RESOURCE_DISK = "disk"


from settings_local import *
