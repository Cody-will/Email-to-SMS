import config
import sms
import json
import random
file = 'quotes.json'
people = config.people
account = config.account


def get_random_quote():
    with open(file, 'r') as data:
        quotes = json.load(data)
        quote = random.choice(list(quotes.items()))
        return ''.join(quote[0] + ' - ' + quote[1]).encode('utf-8')


sms.send_message(people['name'], get_random_quote(), account)
