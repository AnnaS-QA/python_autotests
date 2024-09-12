import requests
import pytest


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3ae6ed885dc5f8b8f043b8989eef9ba6'
HEADER = {'Content-Type': 'application/json','trainer_token':TOKEN}
TRAINER_ID = 4468


def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
assert response.status_code == 200


def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
assert response_get.json()['trainer_id'] == 4468

 