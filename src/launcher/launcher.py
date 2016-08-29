# -*- coding: utf-8 -*-
import sys
import time
import signal
from threading import Thread

try:
    from mesos.native import MesosExecutorDriver, MesosSchedulerDriver
    from mesos.interface import Executor, Scheduler
    from mesos.interface import mesos_pb2
except ImportError:
    from mesos import Executor, MesosExecutorDriver, MesosSchedulerDriver, Scheduler
    import mesos_pb2

from scheduler import ChimeScheduler
from settings import log
from settings import MESOS_HOST


class ChimeLauncher(object):
    """launcher to boot web service and mesos scheduler"""
    def __init__(self, user, name):
    	super(ChimeLauncher, self).__init__()
    	self.framework = mesos_pb2.FrameworkInfo()
    	self.framework.user = user
    	self.framework.name = name
    	
    def shutdown(self, signal, frame):
    	log.info("Chime is shutting down")
    	self.driver.stop()
    
    def launch(self):
        log.info("Chime is launching")
    	scheduler = ChimeScheduler()
    	self.driver = MesosSchedulerDriver(scheduler, self.framework, MESOS_HOST)

    	def run_driver_async():
    		status = 0 if self.driver.run() == mesos_pb2.DRIVER_STOPPED else 1
    		self.driver.stop()
    		sys.exit(status)
    	
    	framework_thread = Thread(target = run_driver_async, args = ())
    	framework_thread.start()

        shutdown = lambda s,f: self.shutdown(s, f)
    	signal.signal(signal.SIGINT, shutdown)
        #while True:
        #	time.sleep(1)
    	while framework_thread.is_alive():
    		time.sleep(1)		
