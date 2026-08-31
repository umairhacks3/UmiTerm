import os
import subprocess


class UmiShell:

    def __init__(self):
        self.running = True

    def show_prompt(self):
        current_dir = os.getcwd()
        return f"umi:{current_dir}$ "

    def execute(self, command):

        command = command.strip()

        if not command:
            return

        if command == "exit":
            self.running = False
            return

        if command == "clear":
            os.system("clear")
            return

        if command == "help":
            self.show_help()
            return

        try:
            subprocess.run(command, shell=True)

        except Exception as error:
            print(f"Error: {error}")

    def show_help(self):

        print()
        print("UmiTerm Shell")
        print("=============")
        print("help")
        print("clear")
        print("exit")
        print()
