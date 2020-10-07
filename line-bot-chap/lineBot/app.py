import json, os, logging
from RandomWordGenerator import RandomWord
from request import post

rw = RandomWord(max_word_size = 6)
def reply(accessToken, replyToken):
    

def answer(event, context):


    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
