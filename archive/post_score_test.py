import requests

base_url = 'http://127.0.0.1:5000/api/'

request1 = requests.post(base_url + 'submit_result', json={'winner': 'Jenn Ifer', 'loser':'Damien', 'score':'21-18',
                                                            'match_date': '2018-08-28', 'who_entered': 'Brett',
                                                            'who_challenged': 'Jenn Ifer'})
print(request1.text)
