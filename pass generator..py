import random
import string

def generate_password(length):
    # characters defined for the password
    char = string.ascii_letters + string.digits + string.punctuation

    # Randomly choose characters from the possible options
    password = ''.join(random.choice(char) for i in range(length))

    return password

def password_generator():
    # takin input from user of the desired password length
    length = int(input("Enter the desired password length: "))

    # Generating password
    password = generate_password(length)

    #output
    print(f"Your generated password is: {password}")

    #pause so thAT USER CAN SEE THE OUTPUT
    input("\n press enter key to exit ")

# Run the password generator
password_generator()
