

class OfferProcessor(object):
	"""processes each offer and generates a corresponding task"""
	def __init__(self, driver):
		super(OfferProcessor, self).__init__()
		self.driver = driver

	def processOffers(self, driver, task, offers):
		for offer in offers:



	def processOffer(self, task, pb_offer):
		offer = Offer(pb_offer).match(task)


	def acceptOffer(self, offer, task):
		self.driver.launchTasks(offer.id, task)

	def declineOffer(self, offer):
		self.driver.declineOffer(offer.id)
