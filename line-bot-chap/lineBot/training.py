import pickle
from s3bz.s3bz import S3
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

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

pickleChatbot = pickle.dumps(chatbot)
pickleChatbotDict = {"pickleChatbot": pickleChatbot}
S3.save(
key = 'chatBotTrained',
objectToSave = pickleChatbotDict,
bucket = 'Trained-Bot'
)