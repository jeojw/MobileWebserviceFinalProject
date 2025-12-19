import requests

class Sender:
    def __init__(self, server_url, api_key):
        self.url = server_url
        self.api_key = api_key

    def send(self, image_path, change_type):
        files = {"image": open(image_path, "rb")}
        data = {"type": change_type, "key": self.api_key}

        res = requests.post(self.url, files=files, data=data)
        return res.status_code, res.text