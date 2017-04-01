from apiai_toolkit import *
import action_methods

while True:
    message = raw_input("User ::  ")
    response = send_message(message)

    if response["status"]["code"] == 200:
     reply_message = response["result"]["fulfillment"]["speech"]
     intent = None
     action = None
     entitiy = None
     try:
         intent,action,entitiy = get_intent_action_entity(response)
     except KeyError:
         print "Bot  ::  " + reply_message
         continue

    if action:
        try:
            methodToCall = getattr(action_methods,action)
            outcome = methodToCall(entitiy)
            reply_message = format_message(action,reply_message,outcome)
        except AttributeError:
            pass

    print "Bot  ::  " + reply_message
