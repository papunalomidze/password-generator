import secrets
import string

def generate( length, number, alpha, symbols):
    if length < 8:
        return "password should be minumum 8 characters"
    
    approved = ""
    if number:
        approved += string.digits
    
    if alpha:
        approved += string.ascii_letters

    if symbols:
        approved += string.punctuation

    password = ""
    if approved:
        for i in range(length):
            password += secrets.choice(approved) 
            print(password + 'here')
        else:
            password = "No characters selected for password generation"

    print(password)