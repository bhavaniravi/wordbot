import recastai
import requests
import api_key



def make_thesaurus_api_call(word):
    url = "http://thesaurus.altervista.org/thesaurus/v1?word="+word+"&language=en_US&key="+api_key.API_KEY+"&output=json"
    return requests.get(url)

def get_thesaurus_detail(word):
    response = make_thesaurus_api_call(word)
    response = response.json()["response"][0]["list"]
    return response["synonyms"].split("|")[0],response["category"]

def get_meaning(word):
    synonym,POS = get_thesaurus_detail(word)
    return synonym


while True:
    message = raw_input("User ::  ")
    client = recastai.Client(api_key.RECAST_KEY, 'en')
    response = client.text_converse(message)
    reply = response.reply()
    intent = response.intent()
    if intent:
        try:
            word = response.entities[0].value
        except:
            print("Bot  ::  "+reply)
            continue
        print reply
        if intent.slug == "thesaurus":
             synonym,POS = get_thesaurus_detail(word)
             reply = reply.replace("*thesaurus*","\nSynonym : "+synonym+"\nParts of speech : "+POS)
        elif intent.slug == "meaning":
             meaning = get_meaning(word)
             reply = reply.replace("{{meaning}}",meaning)
             reply = reply.replace("{{word}}",word)
    print("Bot  ::  "+reply)
