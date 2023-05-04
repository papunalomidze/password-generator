# generate.py

import secrets
import string

def generate( length, number, alpha_upper, alpha_lower, symbols):
    approved = ""
    if number:
        approved += string.digits
    
    if alpha_upper:
        approved += string.ascii_uppercase

    if alpha_lower:
        approved += string.ascii_lowercase

    if symbols:
        approved += string.punctuation

    password = ""
    for i in range(int(length)):
        password += secrets.choice(approved) 

    return password