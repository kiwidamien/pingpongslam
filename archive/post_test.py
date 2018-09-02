import requests

base_url = 'http://127.0.0.1:5000/'

request1 = requests.post(base_url + 'submit_result', json={'who_entered': 'damien'})
print(request1.text)
