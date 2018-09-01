import requests

base_url = 'http://127.0.0.1:5000/api/'

request1 = requests.post(base_url + 'submit_result', json={'winner': 'jwong', 'loser':'damien', 'score':'21-18',
                                                            'match_date': '2018-08-28', 'who_entered': 'brett',
                                                            'who_challenged': 'jwong'})
print(request1.text)
