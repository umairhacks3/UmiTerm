

import json
import os


class PackageManager:

    def __init__(self):

        self.base_dir = os.path.expanduser("~/.umiterm")

        self.db_file = os.path.join(
            self.base_dir,
            "packages.json"
        )

        project_root = os.path.dirname(
            os.path.dirname(
                os.path.dirname(__file__)
            )
        )

        self.repository_file = os.path.join(
            project_root,
            "packages",
            "repository",
            "index.json"
        )

        os.makedirs(
            self.base_dir,
            exist_ok=True
        )

        if not os.path.exists(self.db_file):

            with open(self.db_file, "w") as file:
                json.dump({}, file, indent=4)

    # -------------------------
    # Database
    # -------------------------

    def load_packages(self):

        with open(self.db_file, "r") as file:
            return json.load(file)

    def save_packages(self, packages):

        with open(self.db_file, "w") as file:
            json.dump(
                packages,
                file,
                indent=4
            )

    # -------------------------
    # Repository
    # -------------------------

    def load_repository(self):

        if not os.path.exists(
            self.repository_file
        ):
            return {}

        with open(
            self.repository_file,
            "r"
        ) as file:

            return json.load(file)

    # -------------------------
    # List
    # -------------------------

    def list_packages(self):

        packages = self.load_packages()

        if not packages:

            print(
                "No packages installed."
            )
            return

        print(
            "Installed Packages"
        )
        print(
            "=================="
        )

        for name, info in packages.items():

            print(
                f"{name} - "
                f"{info['version']}"
            )

    # -------------------------
    # Search
    # -------------------------

    def search(self, name):

        repository = self.load_repository()

        found = False

        for package_name, info in repository.items():

            if name.lower() in package_name.lower():

                print(
                    f"{package_name} - "
                    f"{info['version']}"
                )

                print(
                    f"  {info['description']}"
                )

                found = True

        if not found:

            print(
                f"No package found: {name}"
            )

    # -------------------------
    # Install
    # -------------------------

    def install(self, name):

        repository = self.load_repository()

        packages = self.load_packages()

        if name not in repository:

            print(
                f"Package not found: {name}"
            )
            return

        if name in packages:

            print(
                f"{name} is already installed."
            )
            return

        info = repository[name]

        packages[name] = {
            "version": info["version"],
            "description": info["description"]
        }

        self.save_packages(packages)

        print(
            f"Installed {name} "
            f"version {info['version']}"
        )
