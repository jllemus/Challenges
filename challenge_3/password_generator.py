import random
def password_generator():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?!*-_¡¿='
    pass_length = 10
    password = ''
    for i in range(0, pass_length):
        password += random.choice(letters)
    return password
print(password_generator())