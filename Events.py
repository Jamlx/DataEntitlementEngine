from Event import Event

#This file will be used to create and store different Events. This file can then be imported to be used elsewhere.

events = {}

#Default Error Type
errors = {
	"paramError": {
		"error": "Parameter Error: Validate provided parameters are correct and valid",
		"value": "Error: See error or details for more info"
	}
}

#Testing Function (Will use 2 params: param1 and param2
testingFuncName = "testingFunc"
def testingFunc(user, params):
	output = {}
	try:
		fname = user.fname
		lname = user.lname
		email = user.email
		param1 = params["param1"]
		param2 = params["param2"]
	except:
		return errors["paramError"]
	print("param1 is: " + str(param1))
	print("param2 is: " + str(param2))
	print("user data: " + fname + " " + lname + " " + email)
	output["error"] = "None"
	output["value"] = "Items printed with no errors."
	return output
testingFuncLevel = 4
testingFuncDesc = "This testing function is just to test things."
testingFuncEvent = Event(testingFuncName, testingFunc, testingFuncLevel, testingFuncDesc)
events[testingFuncEvent.name] = testingFuncEvent
