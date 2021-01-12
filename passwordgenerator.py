import random
import os
import pyperclip

chars = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%&'

os.system('clear')
print('Number of passwords?')
number = int(input('[1]') or '1')


print('Password length?')
length = int(input('[20]') or '20')

print('---')
for p in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    pyperclip.copy(password)
    print(password)
print('---')
print('The last password is sent to your clipboard')
