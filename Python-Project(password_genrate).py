import random


chars = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*().,:'

number = int(input('Number of password to generate: ')) 

length = int(input('input your password length: '))


print('\nhere are your password')

for pws in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)

    print(password)   