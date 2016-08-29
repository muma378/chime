# -*- coding: utf-8 -*-

import threading

try:
	from mesos.native import MesosExecutorDriver
	from mesos.interface import Executor
	from mesos.interface import mesos_pb2
except ImportError:
	from mesos import Executor, MesosExecutorDriver
	import mesos_pb2

from settings import log


class ChimeExecutor(Executor):

	def registered(self, driver, executorInfo, frameworkInfo, slaveInfo):
		self.hostname = executorInfo.name.value



	def reregistered(self, driver, slaveInfo):
	"""
	Invoked when the executor re-registers with a restarted slave.
	"""


	def disconnected(self, driver):
	"""
	Invoked when the executor becomes "disconnected" from the slave (e.g.,
	the slave is being restarted due to an upgrade).
	""" 
		log.info("Executor is disconnected")


	def launchTask(self, driver, task):
		def run():
			log.info("Task {taskId} is running on {hostname}".format(
				taskId=task.task_id.value, hostname=self.hostname))
			return

		thread = threading.Thread(target=run)
		thread.start()

	def killTask(self, driver, taskId):
	"""
	Invoked when a task running within this executor has been killed (via
	SchedulerDriver.killTask).  Note that no status update will be sent on
	behalf of the executor, the executor is responsible for creating a new
	TaskStatus (i.e., with TASK_KILLED) and invoking ExecutorDriver's
	sendStatusUpdate.
	"""


	def frameworkMessage(self, driver, message):
	"""
	Invoked when a framework message has arrived for this executor.  These
	messages are best effort; do not expect a framework message to be
	retransmitted in any reliable fashion.
	"""

	def shutdown(self, driver):
	"""
	Invoked when the executor should terminate all of its currently
	running tasks.  Note that after Mesos has determined that an executor
	has terminated any tasks that the executor did not send terminal
	status updates for (e.g., TASK_KILLED, TASK_FINISHED, TASK_FAILED,
	etc) a TASK_LOST status update will be created.
	"""

	def error(self, driver, message):
	"""
	Invoked when a fatal error has occurred with the executor and/or
	executor driver.  The driver will be aborted BEFORE invoking this
	callback.
	"""
		print("Error from Mesos: %s" % message, file=sys.stderr)


