import os
import requests
from datetime import datetime

api_address = 'api'
api_port = 8000
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
sentence = "life is beautiful"

def call_and_log(user, password, version):
    url = f'http://{api_address}:{api_port}/{version}/sentiment'
    params = {'username': user, 'password': password, 'sentence': sentence}
    response = requests.get(url, params=params)
    status_code = response.status_code
    result = 'SUCCESS' if status_code == 200 else 'FAILURE'
    return status_code, result

s1, r1 = call_and_log("alice", "wonderland", "v1")
s2, r2 = call_and_log("alice", "wonderland", "v2")
s3, r3 = call_and_log("bob", "builder", "v1")
s4, r4 = call_and_log("bob", "builder", "v2")

if os.environ.get('LOG') == '1':
    with open('./log/log.txt', 'a') as f:
        f.write(f'[{timestamp}] alice -> /v1 => {s1} {r1}\n')
        f.write(f'[{timestamp}] alice -> /v2 => {s2} {r2}\n')
        f.write(f'[{timestamp}] bob -> /v1 => {s3} {r3}\n')
        f.write(f'[{timestamp}] bob -> /v2 => {s4} {r4}\n')