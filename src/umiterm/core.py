from .shell import UmiShell


VERSION = "0.3"


class UmiTerm:

    def __init__(self):
        self.shell = UmiShell()

    def show_banner(self):

        print("=" * 50)
        print("         UmiTerm v0.3")
        print("   UmiTerm Terminal Environment")
        print("=" * 50)
        print("Type 'help' for commands.")
        print("Type 'exit' to quit.")
        print()

    def start(self):

        self.show_banner()

        while self.shell.running:

            try:

                command = input(
                    self.shell.show_prompt()
                ).strip()

                self.shell.execute(command)

            except KeyboardInterrupt:

                print("\nUse 'exit' to quit.")

            except EOFError:

                print("\nGoodbye!")
                break
