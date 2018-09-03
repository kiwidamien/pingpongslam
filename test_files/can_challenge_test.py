import requests

base_url = 'http://127.0.0.1:5000/api/'

request1 = requests.get(base_url + 'Damien/' + 'can_challenge')
print(request1.text)
