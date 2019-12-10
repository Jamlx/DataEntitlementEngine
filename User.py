class User:
	def __init__(self, id, email, fname, lname, level, title=''):
		self.id = int(id)
		self.email = email
		self.fname = fname
		self.lname = lname
		self.level = int(level)
		self.title = title
		self.notes = []

	def addNote(self, str):
		self.notes.append(str)

	def details(self):
		print("\n====================")
		print("User Details: ")
		print("id: " + str(self.id))
		print("email: " + self.email)
		print("fname: " + self.fname)
		print("lname: " + self.lname)
		print("level: " + str(self.level))
		print("title: " + self.title)
		print("notes { ")
		print(self.notes)
		print("} end notes ")
		print("====================")

