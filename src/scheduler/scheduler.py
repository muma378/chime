# -*- coding: utf-8 -*-

import Queue

try:
    from mesos.native import MesosSchedulerDriver
    from mesos.interface import Scheduler
    from mesos.interface import mesos_pb2
except ImportError:
    from mesos import Scheduler, MesosSchedulerDriver
    import mesos_pb2

from launcher import OfferProcessor
from settings import log

class ChimeScheduler(Scheduler):
    """
    A scheduler is to distribute tasks and executors,    
    """
    def __init__(self):
    	self.queue = Queue.Queue()
        self.offer_processor = OfferProcessor()

    def registered(self, driver, frameworkId, masterInfo):
        log.info("Registed as {frameworkId} to master '{masterId}'"
       	    .format(frameworkId=frameworkId.value, masterId=masterInfo.id))

    def reregistered(self, driver, masterInfo):
        log.info("Re-register to master '{masterId}'".format(masterId=masterInfo.id))

    def resourceOffers(self, driver, offers):
        log.info("Received offers with ${offers}".format(offers=offers))

        
        if not self.queue.empty():
            task = self.queue.get()
        self.offer_processor.processOffers(driver, task, offers)



    def statusUpdate(self, driver, status):
        log.info("Received status update for task {taskId}: {state} ({message})"
            .format(taskId=status.task_id.value,
                state=status.state.value,
                message=status.message.value))


    def frameworkMessage(self, driver, executorId, slaveId, message):
        pass

    def disconnected(self, driver):
        pass

    def offerRescinded(self, driver, offerId):
        pass

    def slaveLost(self, driver, slaveId):
        pass

    def executorLost(self, driver, executorId, slaveId, status):
        pass

    def error(self, driver, message):
        pass
