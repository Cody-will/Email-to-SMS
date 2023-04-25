import json
import random


def get_random_quote(file):
    with open(file, 'r') as data:
        quotes = json.load(data)
        quote = random.choice(list(quotes.items()))
        return ''.join(quote[0] + ' - ' + quote[1]).encode('utf-8')
