import json, os, logging
from requests import post
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pickle
from s3bz.s3bz import S3

accessToken = os.environ['ACCESS_TOKEN']
# pickleChatbotDict = S3.load(
# key = "chatBotTrained",
# bucket = 'trained-bot'
# )
# pickleChatbot = pickleChatbotDict["pickleChatbot"]
# chatbot = pickle.loads(pickleChatBot)
chatbot = ChatBot("lineBotChap", storage_adapter ='chatterbot.storage.SQLStorageAdapter', proprecessors = ['chatterbot.preprocessors.clean_whitespace'], database_uri = 'sqlite:////tmp/databse.db', read_only=True)

# with open(credLocation , 'rb') as f:
#     creden = pickle.load(f)
#     PW = creden['pw']
#     USER = creden['user']
key = 'chatterbotdb.db'
path = '/tmp/databse.db'
bucket = 'trained-bot'
S3.loadFile(key = key, path = path, bucket = bucket)

def reply(accessToken, replyToken, text):
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
