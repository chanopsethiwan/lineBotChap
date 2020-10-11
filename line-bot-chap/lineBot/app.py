import json, os, logging
from RandomWordGenerator import RandomWord
from requests import post
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

accessToken = os.environ['ACCESS_TOKEN']
chatbot = ChatBot("lineBotChap")
conversation = [
    "Hi",
    "Hello",
    "How are you doing?",
    "I'm doing great",
    "Thank you",
    "You're welcome"
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)

def reply(accessToken, replyToken, text):
#     rw = RandomWord(max_word_size = 6)
#     rwgenerated = rw.generate()
#     rwgeneratedupper = rwgenerated.upper()
    response = chatbot.get_response(text)
    url = 'https://api.line.me/v2/bot/message/reply'
    headers = {'Authorization': 'Bearer '+ accessToken}
    data = {
    "replyToken":replyToken,
    "messages":[
        {
            "type":"text",
            "text":response
        }
    ]}
    return post(url = url, headers = headers, json = data)

def answer(event, context):
    lineWebhookObject = json.loads(event['body']) 
    replyToken = lineWebhookObject['events'][0]['replyToken']
    text_by_user = lineWebhookObject['events'][0]['message']['text']
    message = reply(accessToken, replyToken, text_by_user)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message.json(),
        }),
    }
