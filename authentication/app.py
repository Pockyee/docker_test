import os
import requests
from datetime import datetime

api_address = 'api'
api_port = 8000
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

users = [
    ('alice', 'wonderland'),
    ('bob', 'builder'),
    ('clementine', 'mandarine')
]

for username, password in users:
    response = requests.get(
        url=f'http://{api_address}:{api_port}/permissions',
        params={'username': username, 'password': password}
    )
    status_code = response.status_code
    result = 'SUCCESS' if status_code == 200 else 'FAILURE'

    if os.environ.get('LOG') == '1':
        with open('./log/log.txt', 'a') as f:
            f.write(f'[{timestamp}] {username}:{password} => {status_code} {result}\n')