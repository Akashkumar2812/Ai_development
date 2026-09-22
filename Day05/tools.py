from datetime import datetime
import random
def get_current_time():
    """Return the current date and time."""
    return datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

import random
def roll_dice():
    """Return a random number between 1 and 6."""
    return random.randint(1, 6)

import secrets
import string
def generate_password(length=12):
    """Generate a secure random password."""
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )
    password = ""
    for _ in range(length):
        password += secrets.choice(characters)
    return password

def read_text_file(file_path):
    """Read and return the content of a text file."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"