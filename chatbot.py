from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance

chatbot = ChatBot('ChatBot')

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
    "do you know me",
    "yes, you are a humen",
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