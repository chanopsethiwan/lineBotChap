import pickle
from s3bz.s3bz import S3
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("lineBotChap", storage_adapter ='chatterbot.storage.SQLStorageAdapter', proprecessors = ['chatterbot.preprocessors.clean_whitespace'], database_uri = 'sqlite:////tmp/databse.db', read_only=True)
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

# pickleChatbot = pickle.dumps(chatbot)
# pickleChatbotDict = {"pickleChatbot": pickleChatbot}
# S3.save(
# key = 'chatBotTrained',
# objectToSave = pickleChatbotDict,
# bucket = 'trained-bot'
# )

key = 'chatterbotdb.db'
path = '/tmp/databse.db'
bucket = 'trained-bot'
S3.saveFile(key = key, path = path, bucket = bucket)