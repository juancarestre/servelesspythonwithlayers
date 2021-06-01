import sys
sys.path.append('./app/')
import json
from shared.dorequest import doreq
from numpy import array

def lambda_handler(event, context):
    # TODO implement
    r = doreq('https://pokeapi.co/api/v2/pokemon/blastoise')
    print(r)