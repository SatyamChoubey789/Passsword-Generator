import random
import string

def generate_password():
    print("Welcome to the PyPassword Generator!")
    
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))

    # Creating a string containing all possible characters for password generation
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # Generating the password directly using random.choices
    password_list = (
        random.choices(string.ascii_letters, k=nr_letters) +
        random.choices(string.digits, k=nr_numbers) +
        random.choices(string.punctuation, k=nr_symbols)
    )

    # Shuffling the generated password characters
    random.shuffle(password_list)

    # Joining the characters to form the password
    password = ''.join(password_list)
    return password

# Generating and printing the password
generated_password = generate_password()
print(f"Your random password to use is: {generated_password}")
print("Thank You !!! ")
