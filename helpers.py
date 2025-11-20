import random
import string

login = None
password = None

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def store_login(log, passw):
    global login
    global password
    login = log
    password = passw

def get_login():
    return login, password