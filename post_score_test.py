import requests

base_url = 'http://127.0.0.1:5000/'

request1 = requests.post(base_url + 'submit_result', json={'winner': 'jwong', 'loser':'brett', 'score':'18-3',
                                                            'match_date': '2018-08-30', 'who_entered': 'damien',
                                                            'who_challenged': 'brett'})
print(request1.text)
