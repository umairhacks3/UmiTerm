#!/usr/bin/env python3

import os
import subprocess
import json


# ==========================================
# UmiTerm Configuration
# ==========================================

VERSION = "0.2"

UMI_HOME = os.path.expanduser("~/.umiterm")
USERS_DIR = os.path.join(UMI_HOME, "users")
PACKAGES_DIR = os.path.join(UMI_HOME, "packages")
REPOSITORY_DIR = os.path.join(UMI_HOME, "repository")
CONFIG_DIR = os.path.join(UMI_HOME, "config")
CACHE_DIR = os.path.join(UMI_HOME, "cache")


# ==========================================
# UmiTerm Environment
# ==========================================

def setup_environment():

    directories = [
        UMI_HOME,
        USERS_DIR,
        PACKAGES_DIR,
        REPOSITORY_DIR,
        CONFIG_DIR,
        CACHE_DIR
    ]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)


# ==========================================
# User System
# ==========================================

def create_user(username):

    if not username:
        print("Usage: umi user create <username>")
        return

    user_dir = os.path.join(USERS_DIR, username)
    home_dir = os.path.join(user_dir, "home")
    config_dir = os.path.join(user_dir, "config")

    if os.path.exists(user_dir):
        print(f"User already exists: {username}")
        return

    os.makedirs(home_dir)
    os.makedirs(config_dir)

    user_data = {
        "username": username,
        "home": home_dir,
        "config": config_dir
    }

    user_file = os.path.join(user_dir, "user.json")

    with open(user_file, "w") as file:
        json.dump(user_data, file, indent=4)

    print()
    print("User created successfully!")
    print(f"Username : {username}")
    print(f"Home     : {home_dir}")
    print()


def list_users():

    if not os.path.exists(USERS_DIR):
        print("No users found.")
        return

    users = []

    for item in os.listdir(USERS_DIR):

        user_path = os.path.join(USERS_DIR, item)

        if os.path.isdir(user_path):
            users.append(item)

    if not users:
        print("No users found.")
        return

    print()
    print("UmiTerm Users")
    print("-------------")

    for user in sorted(users):
        print(f"- {user}")

    print()


# ==========================================
# Version
# ==========================================

def show_version():

    print()
    print("UmiTerm v" + VERSION)
    print("UmiTerm Terminal Environment")
    print()


# ==========================================
# Help
# ==========================================

def show_help():

    print()
    print("UmiTerm Commands")
    print("================")
    print()
    print("help")
    print("version")
    print("clear")
    print()
    print("umi user create <username>")
    print("umi user list")
    print()
    print("exit")
    print()
    print("Linux commands are also supported.")
    print()


# ==========================================
# Command Processor
# ==========================================

def process_command(command):

    command = command.strip()

    if not command:
        return True

    # Exit

    if command == "exit":
        return False

    # Help

    if command == "help":
        show_help()
        return True

    # Version

    if command == "version":
        show_version()
        return True

    # Clear

    if command == "clear":
        os.system("clear")
        return True

    # Create User

    if command.startswith("umi user create "):

        username = command[len("umi user create "):].strip()

        create_user(username)

        return True

    # List Users

    if command == "umi user list":

        list_users()

        return True

    # Normal Linux command

    try:

        subprocess.run(command, shell=True)

    except Exception as error:

        print(f"Error: {error}")

    return True


# ==========================================
# Main
# ==========================================

def main():

    setup_environment()

    print("=" * 50)
    print("         UmiTerm v0.2")
    print("   UmiTerm Terminal Environment")
    print("=" * 50)
    print("Type 'help' for commands.")
    print("Type 'exit' to quit.")
    print()

    while True:

        try:

            current_dir = os.getcwd()

            command = input(
                f"umi:{current_dir}$ "
            ).strip()

            if not process_command(command):
                print("Goodbye!")
                break

        except KeyboardInterrupt:

            print("\nUse 'exit' to quit.")

        except EOFError:

            print("\nGoodbye!")
            break


# ==========================================
# Start UmiTerm
# ==========================================

if __name__ == "__main__":
    main()
