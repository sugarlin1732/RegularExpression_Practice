import re

def verify_email_address(address):
    pattern = r'^[a-zA-Z0-9][a-zA-Z0-9_\.\-]{2,19}@([a-zA-Z0-9]{2,8}\.)+[a-zA-Z0-9]{2,8}'
    if bool(re.fullmatch(pattern, address)):
        return "valid"
    return "invalid"

testing_set = [
    'test._-@123456.com',
    '&gejp@gmail.com',
    'test##ge@gmail.com'
    'a@gmail.com',
    'aaaaaaaaaaaaaaaaaaaaaaa@gmail.com',
    'test@com',
    'test@gma##il.com',
    'test@123456789.com'
    'test@1.com'
]

