import random
import os
import pyperclip

numbers = '1234567890'
special_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?'
lowercase = 'qwertyuiopasdfghjklzxcvbnm'
uppercase = 'QWERTYUIOPASDFGHJKLZXCVBNM'


os.system('clear')
print('Number of passwords?')
number = int(input('[1]') or '1')


print('Password length?')
length = int(input('[20]') or '20')

# Ask if special characters are needed. Defautl is no.
print('Include special characters? [y/N]')
if input().lower() == 'y':
    add_special = True
else:
    add_special = False

print('---')
for p in range(number):
    password = ''

    if add_special:
        length = length / 4
    else:
        length = length / 3
        
    length = int(length)
    password = ''
    
    for c in range(length):
        password += random.choice(uppercase)
        password += random.choice(lowercase)
        password += random.choice(numbers) 
        if add_special:
            password += random.choice(special_chars)

    password = ''.join(random.sample(password, len(password)))

    pyperclip.copy(password)
    print(password)
print('---')
print('The last password is sent to your clipboard')
