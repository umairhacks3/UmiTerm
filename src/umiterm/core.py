from .shell import UmiShell
from .users import UserManager
from .packages import PackageManager


VERSION = "0.4"


class UmiTerm:

    def __init__(self):
        self.shell = UmiShell()
        self.users = UserManager()
        self.packages = PackageManager()

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

        # Umi commands
        if parts[0] == "umi":

            if len(parts) == 2 and parts[1] == "version":
                print(f"UmiTerm v{VERSION}")
                return

            # User commands
            if len(parts) == 3 and parts[1] == "user":

                if parts[2] == "list":
                    self.users.list_users()
                    return

            if len(parts) == 4 and parts[1] == "user":

                if parts[2] == "create":
                    self.users.create_user(parts[3])
                    return

            # Package commands
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
            print("Available commands:")
            print("  umi version")
            print("  umi user list")
            print("  umi user create <username>")
            print("  umi list")
            print("  umi search <package>")
            print("  umi install <package>")
            return

        # Exit
        if command == "exit":
            self.shell.running = False
            print("Goodbye!")
            return

        # Normal Linux commands
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
