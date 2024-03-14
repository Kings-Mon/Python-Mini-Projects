#      -:   P A S S W O R D     G E N E R A T O R   :- 
# ================================================================================================== #
# Generate strong password using specified letters, numbers and symbols.
# You can also control the numbers of letters, numbers and symbols.

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '=', '+']

print("Welcome to Password Generator!")
n_letters = int(input("How many letters do you want in your password?\n"))
n_numbers = int(input("How many numbers do you want in your password?\n"))
n_symbols = int(input("How many symbols do you want in your password?\n"))

password_list = []
for i in range(1, n_letters+1):
    password_list += random.choice(letters)
for j in range(1, n_numbers+1):
    password_list += random.choice(numbers)
for k in range(1, n_symbols+1):
    password_list += random.choice(symbols)
#print(password_list)

random.shuffle(password_list)
#print(password_list)

password = ""
for char in password_list:
    password += char
print(password)

# ================================================================================================== #

# Another Way to Approach :- 
# Generate strong password using completely random letters, numbers and symbols.

import random
import string

def generate_password(length):
    """Generate a random password with the specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try:
    length = int(input("Enter the length of the password: "))
    if length < 0:
        raise ValueError("Length must be a Positive integer.")
    if length == 0:
        raise ValueError("Length can't be Zero.")
    if length < 4:
        raise ValueError("Password length must be at least 4.")
except ValueError as ve:
    print(ve)
else:
    password = generate_password(length)
    print("Generated Password: ", password)

# ================================================================================================== #
