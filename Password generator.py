import random

def generate_password(length):
    characters =("a", "b", "c", "d", "e", "f", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0","1", "2","3", "4", "5", "6", "7", "8", "9", "!", "@" "#", "$", "%", "^", "&", "*", ")", "(", "-", "_", "+", "=", ",", "<", ">", "/", "?", ".", ";", ":","'", "[", "]", "{", "}", "~", "`")
    
    if length <= 4:
        return "Password length must be at least 5 characters."

    # Use random.choices for repeated characters (more secure than sample)
    password = ''.join(random.choices(characters, k=length))
    return password

# Ask user for desired password length
try:
    user_length = int(input("Enter desired password length: "))
    password = generate_password(user_length)
    print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")
