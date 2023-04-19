# The account info is a tuple with a gmail address as the first value and an app password as the second value.
# You'll have to set up 2FA on your gmail account and set up an app password for the account for it to
# authenticate properly, otherwise it will say your login details weren't accepted.
account = ('youremail@gmail.com', 'yourAppPassword')

# The dict of people takes the name of the person as the key and the value is a tuple with the
# 10-digit phone number and phone carrier, both as strings.
people = {
    'Name': ('1234567890', 'carrier')
}
