import json, os, logging
from RandomWordGenerator import RandomWord
from requests import post

accessToken = os.environ['ACCESS_TOKEN']

def reply(accessToken, replyToken):
    rw = RandomWord(max_word_size = 6)
    rwgenerated = rw.generate()
    rwgeneratedupper = rwgenerated.upper()
    url = 'https://api.line.me/v2/bot/message/reply'
    headers = {'Authorization': 'Bearer '+ accessToken}
    data = {
    "replyToken":replyToken,
    "messages":[
        {
            "type":"text",
            "text":rwgeneratedupper
        }
    ]}
    return post(url = url, headers = headers, json = data)

def answer(event, context):
    lineWebhookObject = json.loads(event['body'])
    replyToken = lineWebhookObject['events'][0]['replyToken']
    message = reply(accessToken, replyToken)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message.json(),
        }),
    }
