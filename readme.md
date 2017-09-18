# Wordbot

A chatbot that gets you meaning, synonym and antonym of words

## Description

Wordbot uses [Api.ai](http://api.ai) for natural language understanding.
It used python nltk wordnet corpous to get meaning synonym and antonym of words

This wordbot is like a "Hello world" program for building chatbot.

### Setup

This application is built using python2.You need python 2 to be installed in your system.

If not you can create a virtualenv with python2 and use it

1.  Install all required packages  
    `pip install -r requirement.txt`

2.  To download nltk wordnet corpora  
    open python shell  
    `import nltk`
     `nltk.download()`  
3. It will open a dialog box.(Some cases of linux opens a shell prompt)
4. Download `wordnet` under corpora tab
5. To run the application run  
    `python app.py`

This will run your application.

### Training Your bot

For your bot to understand natural language you need to train it.

1. Create a account in [Api.ai](http://api.ai)
2. Create a new agent
3. Go to settings > import & export 
4. Import training data `training.zip` file
5. Once you import it you have your agent trained to get you meanings and opposites
6. To train it furthuer create new intents, entities etx.,
7. For your training to take effect change `CLIENT_ACCESS_TOKEN` under `apiai_toolkit.py`
