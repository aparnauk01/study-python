import random
import string

def get_password(length):
    digits = string.digits
    chars =string.ascii_letters
    special = string.punctuation
    list_of_strings = digits+chars+special
    password = ''
    for a in range(length):
        password+= random.choice(list_of_strings)
    print(password)

num_of_pwds = int(input('Enter the number of password to be genarted: '))

while num_of_pwds > 0:
    length = int(input('Enter the length of password'))
    get_password(length)
    num_of_pwds-=1

