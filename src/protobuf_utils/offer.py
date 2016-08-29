
try:
	from mesos.interface import mesos_pb2
except ImportError:
	import mesos_pb2

from protobuf_utils import BaseProtoBuf

class Offer(BaseProtoBuf):
	"""deserialize the protobuf object of offer"""
	def __init__(self, pb_offer):
		super(Offer, self).__init__()
		self.pb_offer = pb_offer
		
	def deserialize(self):
		pass

	def serialize(self):
		pass