class ExFile:

	def __init__(self, name):
		self.name = name
		self.columns = []

	def __repr__(self):
		return self.name