import random
import string

def generate_password(length=12):
    # Define the character sets for the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = "!@#$%^&*()_+[]{}|;':,.<>?`~"

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate a password with random characters from the combined set
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

# Example usage: Generate a 16-character password
password = generate_password(16)
print(password)