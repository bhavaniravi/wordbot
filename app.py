from flask import Flask
from flask import render_template,jsonify,request
import requests
import action_methods

app = Flask(__name__)
from wordbot import send_message,get_intent_action_entity,format_message

@app.route('/')
def hello():
    """
    Sample flask hello world
    """
    return render_template('home.html')


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

def processRequest(req):
    entity = None
    response_message = None
    comapany_key = None
    contextOut = req["result"]["contexts"]
    if req["result"]["action"] == "get_meaning":
        entity = req["result"]["parameters"]["word"]
        print entity
        response_message = actions.get_meaning(entity)

    return {"speech": response_message,
            "displayText": response_message,
            # "data": data,
            "contextOut": contextOut,
            "source": "webbot-api"
            }

@app.route('/webhook',methods = ["POST"])
def webhook():
    req = request.get_json(silent=True, force=True)
    print("Request:")
    print(json.dumps(req, indent=4))
    res = processRequest(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    print res
    r.headers['Content-Type'] = 'application/json'
    return r

@app.route('/chat',methods=["POST"])
def chat():
    """
    chat end point that performs NLU using rasa.ai
    and constructs response from response.py
    """
    message = request.form["text"]
    response = send_message(message)
    if response["status"]["code"] == 200:
        reply_message = response["result"]["fulfillment"]["speech"]
        try:
            intent,action,entitiy = get_intent_action_entity(response)
        except KeyError:
            pass
        print intent,entitiy,action
        if action:
            methodToCall = getattr(action_methods,action)
            outcome = methodToCall(entitiy)
            reply_message = format_message(action,reply_message,outcome)
        print reply_message
        return jsonify({"status":"success","response":reply_message})

app.config["DEBUG"] = True
if __name__ == "__main__":
    app.run(port=8000)
