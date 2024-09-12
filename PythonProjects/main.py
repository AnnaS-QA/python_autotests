import requests


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3ae6ed885dc5f8b8f043b8989eef9ba6'
HEADER = {'Content-Type': 'application/json','trainer_token':TOKEN}
BODY_create = {
    "name": "Юпи",
    "photo_id": 9
}
BODY_change = {
    "pokemon_id": "70248",
    "name": "ЮпиЮпи",
    "photo_id": 10
}
BODY_pokeball = {
    "pokemon_id": "70248"
}


'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = BODY_create)
print(response_create.text)'''


'''message = response_create.json()['message']
print(message)'''


'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = BODY_change)
print(response_change.text)'''


response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = BODY_pokeball)
print(response_pokeball.text)