import json
from collections import namedtuple
import requests


def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())


def json2obj(data): return json.loads(data, object_hook=_json_object_hook)


api_key = ''
oauth_token = ''
board_id = ''

response = requests.get(
    'https://api.trello.com/1/boards/' + board_id + '/cards?fields=name,badges&key=' + api_key + '&token=' + oauth_token)

cards = json2obj(response.content)
for card in cards:
    if card.badges.attachments > 0:
        print(card.name)
