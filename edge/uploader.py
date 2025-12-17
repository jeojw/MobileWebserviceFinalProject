import requests

SERVER_URL = "https://your_pythonanywhere.com/api/upload/"

def upload_image(filepath):
    files = {'image': open(filepath, 'rb')}
    response = requests.post(SERVER_URL, files=files)
    print("Server:", response.status_code)
