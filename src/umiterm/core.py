from .shell import UmiShell
from .users import UserManager


VERSION = "0.3"


class UmiTerm:

    def __init__(self):
        self.shell = UmiShell()
        self.users = UserManager()

    def show_banner(self):

        print("=" * 50)
        print("         UmiTerm v0.3")
        print("   UmiTerm Terminal Environment")
        print("=" * 50)
        print("Type 'help' for commands.")
        print("Type 'exit' to quit.")
        print()

    def handle_command(self, command):

        parts = command.split()

        # -------------------------
        # Umi commands
        # -------------------------

        if parts and parts[0] == "umi":

            if len(parts) == 2 and parts[1] == "version":
                print(f"UmiTerm v{VERSION}")
                return

            if len(parts) == 3 and parts[1] == "user" and parts[2] == "list":
                self.users.list_users()
                return

            if len(parts) == 4 and parts[1] == "user" and parts[2] == "create":
                self.users.create_user(parts[3])
                return

            print("Unknown Umi command.")
            print("Try: umi version")
            print("     umi user list")
            print("     umi user create <username>")
            return

        # -------------------------
        # Normal shell commands
        # -------------------------

        self.shell.execute(command)

    def start(self):

        self.show_banner()

        while self.shell.running:

            try:

                command = input(
                    self.shell.show_prompt()
                ).strip()

                if not command:
                    continue

                self.handle_command(command)

            except KeyboardInterrupt:

                print("\nUse 'exit' to quit.")

            except EOFError:

                print("\nGoodbye!")
                break
