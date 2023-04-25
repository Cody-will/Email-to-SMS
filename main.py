from Config import config
import sms
from Quotes import quotes

file = 'Quotes/quotes.json'
people = config.people
account = config.account
person = config.people['Name']


def get_message(json_file):
    quote = quotes.get_random_quote(json_file)
    return quote


sms.send_message(person, get_message(file), account)
