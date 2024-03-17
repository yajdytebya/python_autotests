import requests
import pytest

TOKEN = ''
URL = 'https://api.pokemonbattle.me/v2'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200
    
def test_part_of_response():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': 183})
    assert response.json()['data'][0]['trainer_name'] == 'Бибизянка'
