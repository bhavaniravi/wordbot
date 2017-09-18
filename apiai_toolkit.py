import apiai
import random
import json
import requests

CLIENT_ACCESS_TOKEN = "f60d8f1610c44081af5d42d61631e91a"
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

SESSION_ID = str(random.randint(2,999))

def format_message(action,reply_message,outcome):
    """
    formats output message depending on the action
    """
    try:
        reply_message = reply_message.replace(action,outcome[0])
    except IndexError:
        reply_message = "Oops !! That is not a proper word I couldn't find anything about it in the Dictionary"
    return reply_message

def get_intent_action_entity(response):
    """
    given apiai response returns intent,entity,action
    """
    action = None
    entitiy = None
    try:
        intent = response['result']['metadata']['intentName']
    except KeyError:
        intent = None

    try:
        action = response["result"]["action"]
    except KeyError:
        action = None

    try:
        entitiy = response["result"]["parameters"]['word']
    except KeyError:
        try:
             for context in response["result"]["contexts"]:
                if context["name"] == "word":
                    entitiy = context["parameters"]['word']
                    break
        except KeyError as e:
            print e
            entitiy = None
    return intent,action,entitiy


def send_message(message):
    """
    Sends user text message to api.ai and gets NLU information
    """
    request = ai.text_request()
    request.session_id = SESSION_ID
    request.query = message
    response = request.getresponse()
    raw_response = response.read()
    print raw_response
    return json.loads(raw_response)
