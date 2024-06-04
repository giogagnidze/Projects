import random

def letters():
    return "qwertyuiopasdfghjklzxcvbnm"

def big_letters():
    return "QWERTYUIOPASDFGHJKLZXCVBNM"

def numbers():
    return "0123456789"
    
def random_symbols():
    return "!@#$%^&*()"

def generate_password(length):
    password_characters = letters() + big_letters() + numbers() + random_symbols()
    password = "".join(random.sample(password_characters, length))
    return password

def main():
    length = int(input("Enter the length of the password: ")) 
    password = generate_password(length)
    print("Your password is:", password)

main()
