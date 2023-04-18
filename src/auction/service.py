import requests
from app import config
from flask import redirect


def process_request():
    try:
        return redirect(get_highest_bidder(), 302)
    except:
        raise Exception()


def get_highest_bidder():
    highest_bidder_url = ''
    highest_bidder_value = -1
    for _ in range(0, int(config.config['bidder_count'])):
        response = get_bidder()
        if (response['bid'] > highest_bidder_value):
            highest_bidder_value = response['bid']
            highest_bidder_url = response['url']
    return highest_bidder_url


def get_bidder():
    r = requests.get(config.config['bidder_url'])
    return r.json()
