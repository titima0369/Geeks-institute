import sys
import getpass
from db import init_db, get_user, create_user
from utils import hash_password, verify_password

def prompt_username():
    while True:
        u = input("Username: ").strip()
        if u:
            return u

def prompt_password(hidden=True):
    if hidden:
        return getpass.getpass("Password: ")
    return input("Password: ")

def signup_flow():
    while True:
        username = prompt_username()
        if get_user(username):
            print("Username already exists. Pick another.")
            continue
        password = prompt_password()
        password2 = getpass.getpass("Confirm password: ")
        if password != password2:
            print("Passwords do not match. Try again.")
            continue
        if create_user(username, hash_password(password)):
            print(f"User '{username}' created successfully.")
            return username

def login_flow():
    username = prompt_username()
    user = get_user(username)
    if not user:
        ans = input("User not found. Sign up? (y/n): ").strip().lower()
        if ans == "y":
            return signup_flow()
        return None
    _, u_name, hashed = user
    password = prompt_password()
    if verify_password(password, hashed):
        print("You are now logged in.")
        return u_name
    else:
        print("Incorrect password.")
        return None

def main_loop():
    init_db()
    logged_in = None
    print("Commands: login / signup / whoami / exit")
    while True:
        cmd = input("> ").strip().lower()
        if cmd == "exit":
            print("Exiting.")
            break
        if cmd == "login":
            user = login_flow()
            if user:
                logged_in = user
        elif cmd == "signup":
            user = signup_flow()
            if user:
                logged_in = user
        elif cmd == "whoami":
            print(f"Logged in as: {logged_in}" if logged_in else "Not logged in.")
        else:
            print("Unknown command.")

if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        sys.exit(0)
