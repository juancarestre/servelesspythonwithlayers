import sys, os
sys.path.append('./app/')
from shared.dorequest import doreq

def lambda_handler(event, context):
    # TODO implement
    r = doreq(f'{os.environ["POKEMON_API_URL"]}ditto')
    print(r)
