import json, os, logging
from requests import post
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pickle
from s3bz.s3bz import S3

accessToken = os.environ['ACCESS_TOKEN']
pickleChatbotDict = S3.load(
key = "chatBotTrained",
bucket = 'trained-bot'
)
pickleChatbot = pickleChatbotDict['pickleChatBot']
chatbot = pickle.loads(pickleChatBot)

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
