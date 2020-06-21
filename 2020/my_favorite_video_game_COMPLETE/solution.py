import requests

s = requests.Session()

base_url = 'http://steam-origin.contest.tuenti.net:9876/'
route = 'games/cat_fight/get_key'

headers = {
    'X-Forwarded-For': 'pre.steam-origin.contest.tuenti.net:9876',
    'Host': 'pre.steam-origin.contest.tuenti.net:9876'
}

response = s.get(base_url + route, headers=headers)

print(response.text)
