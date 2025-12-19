import requests

SERVER_URL = "http://127.0.0.1:8000/api/upload/"

def upload_image(filepath):
    with open(filepath, 'rb') as f:
        files = {'image': f}
        response = requests.post(SERVER_URL, files=files)

    print("Upload status:", response.status_code)
