import random
import string
import time
import os
import pyfiglet # Remember to execute 'pip install pyfiglet'
import pyansi3  # Remember to execute 'pip install py-ansi3'
from pyansi3 import print_colored

os.system("cd /sdcard") # change this to 'desktop' if you're using PC
os.system("pyfiglet -c BLUE WQB GENERATOR")
print_colored("\033[1;37m\033[0;34m» \033[1;37mThis script is made by {green}MohamedLunar\033[1;37m for generate usernames for instagram, tiktok etc.. and strong passwords and passwords will be saved in {yellow}password.txt\033[1;37m file, same thing for usernames but in {yellow}username.txt \033[1;37mfile\n\n")
print_colored("\033[1;37m{red}YouTube{reset}: \033[1;37mhttps://youtube.com/MohamedLunar\n")
print_colored("\033[1;37m{green}GitHub{reset}: \033[1;37mhttps://github.com/MohamedLunar\n")
print_colored("\033[1;37m{yellow}Source Code{reset}: \033[1;37mhttps://github.com/MohamedLunar/wqb-generator")

user_input = int(input("\n\n\033[0;34m[\033[1;37m1\033[0;34m] \033[1;37mpassword generator     \033[0;34m[\033[1;37m2\033[0;34m] \033[1;37musername generator\n\n\033[0;34m» \033[1;37mSo what choose you want to try? "))


def generate_password(length=12):
    if length < 4:  # Ensure the password has enough characters
        raise ValueError("Password length should be at least 4.")

    # Define character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits

    # Ensure the password has at least one of each type of character
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits)
    ]

    # Fill the rest of the password length with random choices from all allowed characters
    all_characters = uppercase + lowercase + digits
    password += random.choices(all_characters, k=length - 3)

    # Shuffle the characters to make the password unpredictable
    random.shuffle(password)

    return ''.join(password)

# Example usage
if user_input == 1:
	os.system("clear")
	os.system("pyfiglet -c RED PASSWORD GEN")
	password_length = 10
	password = generate_password(password_length)
	print("\033[1;33m==================================\n\033[0;32mGenerated Password:\033[0;36m", password + "\n\033[0;32mCheck \033[0;35mpassword.txt \033[0;32mfile to find it\n\033[1;33m==================================")
	
	with open("password.txt", "w") as f:
		f.write(password)

def generate_username(length=4):
    # Define allowed character sets
    letters = string.ascii_lowercase
    digits = string.digits
    symbols = "._"
    all_characters = letters + digits + symbols

    # Generate a random username of the specified length
    return ''.join(random.choices(all_characters, k=length))

green = "{bold}{green}"

def infinite_username_generator():
    i = 1  # Counter for username number
    try:
        with open("usernames.txt", "a", buffering=1) as file:  # Open file in append mode with line buffering
            while True:
                time.sleep(0.1)
                username = generate_username(length=4)
                print_colored(f"{green}[username {i}] {username}")
                file.write(username + "\n")  # Save username to the file
                i += 1
    except KeyboardInterrupt:
        print("\nUsername generation stopped.")

# Start infinite username generation
if user_input == 2:
	os.system("clear")
	os.system("pyfiglet -c RED USERNAME GEN")
	infinite_username_generator()