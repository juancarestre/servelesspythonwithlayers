import json
from ..shared.dorequest import doreq

def lambda_handler(event, context):
    # TODO implement
    r = doreq('https://pokeapi.co/api/v2/pokemon/ditto')
    print(r)
