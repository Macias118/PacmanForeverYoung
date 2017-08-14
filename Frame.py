class Frame():

	# properties = (x, y, width, height)
	def __init__(self, prop, c, t):
		self.properties = prop
		self.x = prop[0]
		self.y = prop[1]
		self.width = prop[2]
		self.height = prop[3]
		self.color = c
		self.thickness = t

	def get_prop(self):
		return self.properties

	def get_color(self):
		return self.color

	def get_thickness(self):
		return self.thickness
