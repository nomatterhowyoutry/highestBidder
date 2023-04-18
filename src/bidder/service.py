import random
import string
from app import config

def procces_request(): 
    return {
        'bid': get_random_float(),
        'url': get_random_url(int(config.config['random_bidder_url_range']))
    }


def get_random_float():
    return random.uniform(0, int(config.config['random_bidder_range']))

def get_random_url(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
