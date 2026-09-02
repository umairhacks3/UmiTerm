class UmiAI:

    def __init__(self):
        self.name = "UMI AI"

    def ask(self, question):

        question = question.strip()

        if not question:
            print()
            print("UMI AI: Please ask a question.")
            print()
            return

        print()
        print("UMI AI")
        print("======")

        # Basic local knowledge
        if "python" in question.lower():

            print(
                "Python is a programming language used for "
                "software development, automation, data science, "
                "web development, and many other tasks."
            )

        elif "linux" in question.lower():

            print(
                "Linux is an open-source operating system kernel. "
                "Many operating systems and environments are built "
                "around Linux."
            )

        elif "umiterm" in question.lower() or "umi term" in question.lower():

            print(
                "UMI Term is a developer-focused terminal environment "
                "being developed as an open-source project."
            )

        elif "git" in question.lower():

            print(
                "Git is a version control system used to track changes "
                "in software projects and collaborate with developers."
            )

        else:

            print(
                "I am the UMI AI local prototype."
            )
            print(
                "A full local language model will be connected "
                "to this engine in a future version."
            )

        print()

