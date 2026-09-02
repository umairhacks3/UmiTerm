from .shell import UmiShell
from .users import UserManager
from .packages import PackageManager
from .ai import UmiAI


VERSION = "0.4"


class UmiTerm:

    def __init__(self):
        self.shell = UmiShell()
        self.users = UserManager()
        self.packages = PackageManager()
        self.ai = UmiAI()

    def doctor(self):

        import os
        import shutil
        import platform

        print()
        print("UMI Term System Doctor")
        print("======================")
        print()

        print(f"OS:      {platform.system()} {platform.release()}")
        print(f"Machine: {platform.machine()}")
        print(f"Python:  {platform.python_version()}")
        print()

        checks = {
            "Python": shutil.which("python") or shutil.which("python3"),
            "Git": shutil.which("git"),
            "Shell": os.environ.get("SHELL"),
        }

        for name, value in checks.items():

            if value:
                print(f"[OK]   {name}: {value}")
            else:
                print(f"[WARN] {name}: Not found")

        print()

        if os.path.exists(self.packages.db_file):
            print("[OK]   Package database")
        else:
            print("[WARN] Package database missing")

        if os.path.exists(self.packages.repository_file):
            print("[OK]   Package repository")
        else:
            print("[WARN] Package repository missing")

        print()
        print("Doctor check complete.")
        print()

    def show_help(self):

        print()
        print("=" * 58)
        print("                    UMI TERM HELP")
        print("=" * 58)
        print()

        print("SYSTEM")
        print("  umi version")
        print("  umi doctor")
        print("  umi help")
        print()

        print("AI")
        print('  umi ai "<question>"')
        print()

        print("PACKAGES")
        print("  umi list")
        print("  umi search <package>")
        print("  umi install <package>")
        print()

        print("USERS")
        print("  umi user list")
        print("  umi user create <username>")
        print()

        print("SHELL")
        print("  help")
        print("  clear")
        print("  exit")
        print()

        print("=" * 58)
        print()

    def show_banner(self):

        print("=" * 58)
        print("              UmiTerm v0.4")
        print("          UmiTerm Terminal Environment")
        print("=" * 58)
        print()
        print("          ★ Welcome to UMI Term ★")
        print("             Developed by Umair")
        print()
        print("      Type 'help' to see available commands.")
        print()

    def handle_command(self, command):

        parts = command.split()

        if not parts:
            return

        if parts[0] == "umi":

            if len(parts) == 2 and parts[1] == "version":
                print(f"UmiTerm v{VERSION}")
                return

            if len(parts) == 2 and parts[1] == "doctor":
                self.doctor()
                return

            if len(parts) == 2 and parts[1] == "help":
                self.show_help()
                return

            if len(parts) >= 3 and parts[1] == "ai":
                question = " ".join(parts[2:])
                self.ai.ask(question)
                return

            if len(parts) == 3 and parts[1] == "user":

                if parts[2] == "list":
                    self.users.list_users()
                    return

            if len(parts) == 4 and parts[1] == "user":

                if parts[2] == "create":
                    self.users.create_user(parts[3])
                    return

            if len(parts) == 2 and parts[1] == "list":
                self.packages.list_packages()
                return

            if len(parts) == 3 and parts[1] == "search":
                self.packages.search(parts[2])
                return

            if len(parts) == 3 and parts[1] == "install":
                self.packages.install(parts[2])
                return

            print("Unknown Umi command.")
            print()
            print("Type 'umi help' to see available commands.")
            print()
            return

        if command == "help":
            self.show_help()
            return

        if command == "exit":
            self.shell.running = False
            print("Goodbye!")
            return

        self.shell.execute(command)

    def start(self):

        self.show_banner()

        while self.shell.running:

            try:

                command = input(
                    self.shell.show_prompt()
                ).strip()

                self.handle_command(command)

            except KeyboardInterrupt:

                print("\nUse 'exit' to quit.")

            except EOFError:

                print("\nGoodbye!")
                break
