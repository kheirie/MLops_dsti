import re 

def validate_username(username):
    if not username or ' ' in username:
        return False
    return True

def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Za-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

def validate_email(email):
    if '@' not in email or '.' not in email.split('@')[-1]:
        return False
    return True

def get_username():
    username = input("Enter a user name: ")
    if validate_username(username):
        return username
    return "Invalid username."
    
def get_passowrd():
    password = input("Enter a password: ")
    if validate_password(password):
        return password
    return "Invalid password."
    
    
def get_email():
    email = input("Enter an email address: ")
    if validate_email(email):
        return email
    return "Invalid email."