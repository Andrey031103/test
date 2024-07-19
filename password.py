password='password'

def ask_password():
    user_password = input()
    if user_password == password:
        return True
    else:
        return False

i = 0
while i < 3:
    if ask_password() == True:
        i = 3
    else:
        i = i + 1
