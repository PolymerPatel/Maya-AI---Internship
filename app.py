#app.py

from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from chatbot import ask, append_interaction_to_chat_log

app = Flask(__name__)
app.config['KEY'] = 'XYZ'
@app.route('/bot', methods=['POST'])


def bot():
    incoming_msg = request.values['Body']
    chat_log = session.get('chat_log')

    answer = ask(incoming_msg, chat_log)
    session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer,
                                                         chat_log)

    r = MessagingResponse()
    r.message(answer)
    return str(r)


#chatbot.py (second repo from Maya)

import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.environ.get('OPENAI_KEY')
completion = openai.Completion()

start_chat_log = '''Human: Hello, who are you?
AI: I am doing great. How can I help you today?
'''
def ask(question, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    prompt = f'{chat_log}Human: {question}\nAI:'
    response = completion.create(
        prompt=prompt, engine="davinci", stop=['\nHuman'], temperature=0.9,
        top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
        max_tokens=150)
    answer = response.choices[0].text.strip()
    return answer

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    return f'{chat_log}Human: {question}\nAI: {answer}\n'

home = C:\Users\Owner\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0
include-system-site-packages = false
version = 3.9.9
