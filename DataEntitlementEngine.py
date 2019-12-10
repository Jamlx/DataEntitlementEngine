from Events import events
from User import User
from Event import Event
from Enforcer import Enforcer

john = User(123, "abc@abc.com", "john", "smith", 5, "ceo")
nick = User(321, "cbac@cba.com", "nick", "mann", 1, "cashier")
testingFuncEvent = events["testingFunc"]

johnTestingFuncEnforcer = Enforcer(john, testingFuncEvent, {"param1":"abcabcabcabc", "param2": "123123123123"})
johnTestingFuncEnforcer.details()

nickTestingFuncEnforcer = Enforcer(nick, testingFuncEvent, {"param1":"cbacbacbacba", "param2": "321321321321"})
nickTestingFuncEnforcer.details()

