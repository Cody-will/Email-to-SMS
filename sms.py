import smtplib

carriers = {
    'att': '@mms.att.net',
    'tmobile': '@tmomail.net',
    'verizon': '@vtext.com',
    'sprint': '@page.nextel.com'
}


def send_message(person: tuple, message: str, account: tuple):
    number, carrier = person['number'], person['carrier']
    receiver = f'{number}{carriers[carrier]}'
    message = message
    user, password = account
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(user, password)
    server.sendmail(user, receiver, message)
    server.quit()
