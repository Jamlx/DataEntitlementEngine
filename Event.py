class Event:
	def __init__(self, name, func, level, desc):
		self.name = name
		self.func = func
		self.level = int(level)
		self.desc = desc

	def details(self):
		print("\n====================")
		print("Event Details: ")
		print("name: " + self.name)
		print("level: " + str(self.level))	
		print("desc: " + self.desc)
		print("====================")

