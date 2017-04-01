from apiai_toolkit import *
import action_methods

def processRequest(req):
    if req["status"]["code"] == 200:
        reply_message = response["result"]["fulfillment"]["speech"]
        try:
            intent,action,entitiy = get_intent_action_entity(response)
        except KeyError:
            pass
        print intent,entitiy,action
        if action:
            try:
                methodToCall = getattr(action_methods,action)
                outcome = methodToCall(entitiy)
                reply_message = format_message(action,reply_message,outcome)
            except AttributeError:
                pass
    return {"speech": reply_message,
            "displayText": reply_message,
            # "data": data,
            "contextOut": [entity],
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
