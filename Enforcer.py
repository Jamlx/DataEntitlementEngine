from User import User
from Event import Event

class Enforcer:
	def __init__(self, user, event, params={}):
		self.user = user
		self.event = event
		if(user.level < event.level):
			self.error="Insufficient Permissions: User level too low"
			self.output="Error: See error"
		else:
			print("===== Event Started =====")
			output = event.func(user, params)
			print("===== Event Complete =====")
			self.output = output["value"]
			self.error = output["error"]

	def details(self):
		print("\n========================================")
		print("Enforcer Details: ")
		
		print("output: " + str(self.output))
                print("error: " + str(self.error))		
		
		self.user.details()
		self.event.details()
		
		print("\n========================================")

