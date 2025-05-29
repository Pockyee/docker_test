import os
import requests
from datetime import datetime

api_address = 'api'
api_port = 8000
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

sentences = [
    "life is beautiful",
    "that sucks"   
]

def call_and_log(version, sentence):
    url = f'http://{api_address}:{api_port}/{version}/sentiment'
    params = {'username': 'alice', 'password': 'wonderland', 'sentence': sentence}
    response = requests.get(url, params=params)
    data = response.json()
    score = data.get('score', 0)
    result = 'POSITIVE' if score > 0 else 'NEGATIVE'
    return result

r1 = call_and_log("v1", sentences[0])
r2 = call_and_log("v2", sentences[0])
r3 = call_and_log("v1", sentences[1])
r4 = call_and_log("v2", sentences[1])

if os.environ.get('LOG') == '1':
    with open('./log/log.txt', 'a') as f:
        f.write(f'[{timestamp}] v1/{sentences[0]} => {r1}\n')
        f.write(f'[{timestamp}] v2/{sentences[0]} => {r2}\n')
        f.write(f'[{timestamp}] v1/{sentences[1]} => {r3}\n')
        f.write(f'[{timestamp}] v2/{sentences[1]} => {r4}\n')
