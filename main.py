import random
import string
import hashlib
import os

# Define the path to the password file
PASSWORD_FILE = "passwords.txt"

# Define the character set to choose from
CHAR_SET = string.ascii_letters + string.digits + string.punctuation

def generate_password(length):
    # Generate a password by randomly choosing characters from the character set
    password = ''.join(random.choice(CHAR_SET) for i in range(length))

    return password

def hash_password(password):
    # Hash the password using SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    return hashed_password

def save_password(name, password):
    # Hash the password and write it to the password file
    hashed_password = hash_password(password)
    with open(PASSWORD_FILE, "a") as file:
        file.write(f"{name}: {hashed_password}\n")

def get_password(name):
    # Look up the hashed password in the password file and return it
    with open(PASSWORD_FILE, "r") as file:
        for line in file:
            if line.startswith(name + ": "):
                hashed_password = line[len(name)+2:].strip()
                return hashed_password

    return None

def check_password(name, password):
    # Check if the provided password matches the hashed password in the password file
    hashed_password = get_password(name)
    if hashed_password is None:
        return False

    return hash_password(password) == hashed_password

def main():
    # Create the password file if it doesn't exist
    if not os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "w") as file:
            pass

    # Prompt the user for an action
    while True:
        action = input("Enter 'g' to generate a password, 's' to save a password, 'c' to check a password, or 'q' to quit: ")
        if action == "g":
            # Prompt the user for a password name and length, generate a password, and print it
            name = input("Enter a name for the password: ")
            length = int(input("Enter the length of the password: "))
            password = generate_password(length)
            print(f"Your password for {name} is: {password}")
        elif action == "s":
            # Prompt the user for a password name and password, save the password
            name = input("Enter a name for the password: ")
            password = input("Enter the password: ")
            save_password(name, password)
            print(f"Password saved for {name}")
        elif action == "c":
            # Prompt the user for a password name and password, check if the password is correct
            name = input("Enter a name for the password: ")
            password = input("Enter the password: ")
            if check_password(name, password):
                print("Password correct")
            else:
                print("Password incorrect")
        elif action == "q":
            # Quit the program
            break
        else:
            print("Invalid action, try again")

if __name__ == "__main__":
    main()
#Ashutoshdhepenetwork
