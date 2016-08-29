
class BaseProtoBuf(object):
	"""base class to deserialize protobuf objects"""
	def __init__(self, pb_object):
		super(BaseProtoBuf, self).__init__()
		self.pb_object = pb_object
		
	def deserialize(self):
		pass

	def serialize(self):
		pass