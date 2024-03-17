import requests

TOKEN = ''
URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'Content-Type': 'application/json',
           'trainer_token': TOKEN}
body = {
    "name": "Бейбик",
    "photo": "https://dolnikov.ru/pokemons/albums/955.png"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body)
print(response.text)


body = {
    "pokemon_id": '14232',
    "name": "Eva",
    "photo": "https://dolnikov.ru/pokemons/albums/234.png"
}

response = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body)
print(response.text)


body = {
    "pokemon_id": '14232'
}

response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body)
print(response.text)
