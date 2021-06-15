import sys
sys.path.append('./app/')
import json
from shared.dorequest import doreq
import numpy as np

def lambda_handler(event, context):
    # TODO implement
    r = doreq('https://pokeapi.co/api/v2/pokemon/pikachu')
    print(r)