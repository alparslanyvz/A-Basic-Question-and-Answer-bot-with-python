# Basic Question-Answer bot with python | github.com/alparslanyvz
import random
username = input("Welcome to ChatBot. Whats your name? ---> ")
question_answer = {
    "hi":[f"Hi {username}",f"Hello {username}"],
    "what is your name":["My name is ChatBot","Im ChatBot"],
    "whats your name":["My name is ChatBot","Im ChatBot"],
    "how are you": ["Im fine and you?","Im great, you?","Not bad."],
    "how old are you":["I was created in 2024."],
    "":[],
    "":[],
    "":[],
    "":[],
    

}
print(f"ChatBot is active. You can start chatting.\n--------------------------------------------")
while True:
    question = input(f"{username}: ")
    answers = question_answer.get(question.lower())
    if answers:
        answer = random.choice(answers)
        print(f"ChatBot: {answer}")
        continue
    else:
        print("ChatBot: I'm sorry. I couldn't understand you :( ")
        continue
