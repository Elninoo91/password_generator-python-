import random
import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure at least one character of each type
    password = random.choice(lowercase_letters) + random.choice(uppercase_letters) + random.choice(digits) + random.choice(special_characters)

    # Generate the remaining characters
    remaining_length = length - 4
    characters = lowercase_letters + uppercase_letters + digits + special_characters
    password += ''.join(random.choice(characters) for _ in range(remaining_length))

    return password

# Prompt the user for the desired password length
length = int(input("Enter the desired password length: "))

# File name to store the passwords
file_name = "passwords.txt"

# Generate a password
password = generate_password(length)

# Append the password to the file
with open(file_name, 'a') as file:
    file.write(password + '\n')

print("Password generated and stored in", file_name)
