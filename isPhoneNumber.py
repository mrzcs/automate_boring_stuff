import re

# without RE used
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

# with RE used
def isPhoneNumber2(text):
    # Create a Regex object
    #phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
    mo = phoneNumRegex.search(text) # returns a Match object
    if mo != None:
        #print(mo.group()) # returns a string of the actual matched text.
        return True
    else:
        return False

""" print('415-555-4242 is a phone number')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number')
print(isPhoneNumber('Moshi moshi')) """

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i: i+12]
    #if isPhoneNumber(chunk):
    if isPhoneNumber2(chunk):
        print('Phone number found: ' + chunk)
print('Done')