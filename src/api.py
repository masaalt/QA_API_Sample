import requests
import json

def send_qa_simple_bot(data):
    url = 'http://localhost:8000/ask_simple_bot'
    res = requests.post(url, json = data).json()
    return res
