import apiai
import requests
import random
import action_methods
import json
CLIENT_ACCESS_TOKEN = "f60d8f1610c44081af5d42d61631e91a"
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

SESSION_ID = str(random.randint(2,999))


def send_message(message):
    request = ai.text_request()
    request.session_id = SESSION_ID
    request.query = message
    response = request.getresponse()
    raw_response = response.read()
    return json.loads(raw_response)

def get_intent_action_entity(response):
    intent = response['result']['metadata']['intentName']
    action = response["result"]["action"]
    entitiy = response["result"]["parameters"]['search_word']
    return intent,action,entitiy

def format_message(intent,reply_message,outcome):
    try:
        reply_message = reply_message.replace(intent,outcome[0])
    except IndexError:
        reply_message = "Oops !! That is not a proper word I couldn't find anything about it in the Dictionary"
    return reply_message
# while True:
#     message = raw_input("User ::  ")
#     response = send_message(message)
#
#     if response["status"]["code"] == 200:
#         reply_message = response["result"]["fulfillment"]["speech"]
#         intent = None
#         action = None
#         entitiy = None
#         try:
#             intent,action,entitiy = get_intent_action_entity(response)
#         except KeyError:
#             print "Bot  ::  " + reply_message
#             continue
#
#         methodToCall = getattr(action_methods,action)
#         outcome = methodToCall(entitiy)
#         reply_message = format_message(intent,reply_message,outcome)
#
#
#         # if intent == "get_meaning":
#         #     if outcome["synonym"]:
#         #         reply_message = reply_message.replace("*meaning*",outcome["synonym"])
#         #     else:
#         #         reply_message = "Oops !! That is not a proper word I couldn't find it in the Dictionary"
#         # elif intent == "get_category":
#         #     if outcome["POS"]:
#         #         reply_message = reply_message.replace("*POS*",outcome["POS"])
#         #     else:
#         #         reply_message = "Oops !! That is not a proper word I couldn't find anything about it in the Dictionary"
#         print "Bot  ::  " + reply_message
