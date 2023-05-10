import csv
import getpass
import os
import time
from hashlib import sha512
from pathlib import Path


def userCreate():
    # collecting user input
    username = input("Enter a username: ")
    password = getpass.getpass(prompt="Enter a password: ")

    username = username.upper()

    # hashing the password
    passhash = sha512(password.encode('utf-8')).hexdigest()

    # creating the user file
    with Path('loginData.csv').open('a', newline='') as f:
        writer = csv.writer(f, delimiter=",", quoting=csv.QUOTE_MINIMAL)
        writer.writerow([username, passhash])
        f.close()

    print("User created successfully!")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    return


def userLogin():
    # collecting user input
    username = input("Enter your username: ")
    password = getpass.getpass(prompt="Enter your password: ")

    username = username.upper()
    # hashing the password
    passhash = sha512(password.encode('utf-8')).hexdigest()

    # opening the user file
    with open("loginData.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if username == row[0] and passhash == row[1]:
                print("Login successful!")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                return
        print("Login failed!")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        return


def main():
    choice = input("1. Create a new user\n2. Login\n3. Exit\n>>> ")
    match choice:
        case "1":
            userCreate()
        case "2":
            userLogin()
        case "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()
        case _:
            print("Invalid choice!")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            main()


if __name__ == "__main__":
    main()
