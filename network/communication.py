# communication.py

import requests


class Communication:
    def __init__(self, server_url):
        self.server_url = server_url

    def send_data(self, route, data):
        url = f'{self.server_url}/{route}'
        response = requests.post(url, json=data)
        return response.json()
