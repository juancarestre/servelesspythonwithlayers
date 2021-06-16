import sys, os
sys.path.append('./app/')
from shared.dorequest import doreq
import numpy as np

def lambda_handler(event, context):
    # TODO implement
    r = doreq(f'{os.environ["POKEMON_API_URL"]}pikachu')
    print(r)