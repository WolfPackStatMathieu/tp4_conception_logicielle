import subprocess

import requests

body = {}
server = subprocess.Popen(["python", "manage.py", "runserver"])
response = requests.post("http://127.0.0.1:8000/", data=body)
print(response.status_code)
server.terminate()
