import json
from collections import namedtuple
import requests


def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())


def json2obj(data): return json.loads(data, object_hook=_json_object_hook)


api_key = '5d961ca71bfc7a390e96c18ebae24792'
oauth_token = 'eca5636d148d8465ae5c05c0cb81ed941df378a37ae98ed7415f2d53f2ebb36e'
board_id = '53b3707ff8537f939d782a92'

response = requests.get(
    'https://api.trello.com/1/boards/' + board_id + '/cards?key=' + api_key + '&token=' + oauth_token)

cards = json2obj(response.content)
for card in cards:
    if card.badges.attachments > 0:
        print(card.name)
