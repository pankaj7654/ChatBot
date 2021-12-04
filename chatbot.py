from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance

chatbot = ChatBot('ChatBot')

# chatbot = ChatBot(
#     'ChatBot',
#     storage_adapter='chatterbot.storage.SQLStorageAdapter',
#     logic_adapters=[
#         'chatterbot.logic.MathematicalEvaluation',
#         'chatterbot.logic.TimeLogicAdapter',
#         'chatterbot.logic.BestMatch',
#         {
#             'import_path': 'chatterbot.logic.BestMatch',
#             'default_response': 'I am sorry, but I do not understand. I am still learning.',
#             'maximum_similarity_threshold': 0.90
#         }
#     ],
#     database_uri='sqlite:///database.sqlite3'
# ) 

 # Training with Personal Ques & Ans 
conversation = [
    "Hey",
    "Hello",
    "Hii",
    "Hello dude",
    "How are you",
    "I am fine, and you",
    "How are you doing",
    "I am doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "bye",
    "Ok bye, thank you",
    "I love you",
    "I love you to",
    "do you know me",
    "yes, you are person",
    "You've Dinner",
    "I have internet, I don't need, Thank you",
    "Have you done"
    
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)

# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english'
) 