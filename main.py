import random 
import string
import time

time.sleep(2)

print('Welcome to Password Generator')

time.sleep(2)

print('Generating Password...')

print('Password:')
lower = string.ascii_lowercase
upper = string.ascii_uppercase
symbol = string.punctuation
num = string.digits
chars = lower + upper + num + symbol
# Generate a password of 12 characters
temp = random.sample(chars, 12 )
print(''.join(temp))
