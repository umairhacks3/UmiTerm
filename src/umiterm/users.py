import json
import os


class UserManager:

    def __init__(self):
        self.base_dir = os.path.expanduser("~/.umiterm")
        self.users_file = os.path.join(
            self.base_dir,
            "users.json"
        )

        os.makedirs(self.base_dir, exist_ok=True)

        if not os.path.exists(self.users_file):
            with open(self.users_file, "w") as file:
                json.dump([], file)

    def list_users(self):

        with open(self.users_file, "r") as file:
            users = json.load(file)

        if not users:
            print("No users found.")
            return

        print("UmiTerm Users")
        print("=============")

        for user in users:
            print(f"- {user}")

    def create_user(self, username):

        username = username.strip()

        if not username:
            print("Username cannot be empty.")
            return

        with open(self.users_file, "r") as file:
            users = json.load(file)

        if username in users:
            print(f"User already exists: {username}")
            return

        users.append(username)

        with open(self.users_file, "w") as file:
            json.dump(users, file, indent=4)

        print(f"User created: {username}")
