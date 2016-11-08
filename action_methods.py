import api_key,requests

def make_thesaurus_api_call(word):
    url = "http://thesaurus.altervista.org/thesaurus/v1?word="+word+"&language=en_US&key="+api_key.API_KEY+"&output=json"
    return requests.get(url)

def get_thesaurus_detail(word):
    response = make_thesaurus_api_call(word)
    print response.json
    response = response.json()["response"][0]["list"]
    return response["synonyms"].split("|")[0],response["category"]

def get_synonym(word):
    try:
        synonym,POS = get_thesaurus_detail(word)
        return {"synonym":synonym}
    except KeyError:
        return {"synonym":None}

def get_category(word):
    try:
        synonym,POS = get_thesaurus_detail(word)
        return {"POS":POS}
    except KeyError:
        return {"POS":None}
