import secrets
import string

def generate( length, number, alpha, symbols):
    approved = ""
    if number:
        approved += string.digits
    
    if alpha:
        approved += string.ascii_letters

    if symbols:
        approved += string.punctuation

    password = ""
    for i in range(int(length)):
        password += secrets.choice(approved) 

    return password