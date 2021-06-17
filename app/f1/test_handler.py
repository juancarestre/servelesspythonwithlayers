from app.f1.handler import lambda_handler
import os

def test_handler():
    os.environ['POKEMON_API_URL'] = 'https://pokeapi.co/api/v2/pokemon/'
    assert lambda_handler(True, True)