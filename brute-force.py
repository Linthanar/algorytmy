from numpy import true_divide


secret = 'password'

def login(password):
    if password == secret:
        return True
    else: 
        return False


print(login('aaaaab'))