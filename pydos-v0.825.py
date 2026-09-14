print("PYDOS 0.825")

print("Setting up system...")

ver = "PY-DOS 0.825"

def reset():

    global setup

    try:

        with open("pydos_config.txt", "w") as file:

            print("Writing setup file...")

            file.write("do_setup = True")

            file.write("\nusername = None")

            print("Setup file successfully created.")

            setup = True

    except Exception as error:

        input(f"There was a problem with creating setup file. {error}")



def confirm(prompt):

    while True:

        response = input(f"{prompt} (y/n): ")

        if response in ["yess", "yes", "y", "ye"]:

            return True

            break

        elif response in ["noo", "no", "n"]:

            return False

            break

        else:

            print("That's not a valid respone.")

def com_hub():

    command = input("Type Command: ")

    if command == 'help':

        print(f"All Commands:\n\nshutdown - turns off computer\nsay [input] - the terminal will repeat what you said\nusername - the terminal will say your current username\nreset - resets this computer\n\nYou are using {ver}")

    elif command == 'shutdown':

        user_says = confirm("Are you sure? Any unsaved work will be lost.")

        if user_says == True:

            shutdown()

        elif user_says == False:

            print("Shutdown aborted.")



    elif command == 'username':

        print(username)



    elif command[:3] == 'say':

        what_to_say = command[4:]

        print(what_to_say)

    elif command == 'reset':

        user_says = confirm("Are you sure you want to reset this computer? By resetting, you delete all data from this computer and bring PY-DOS back to setup.")

        if user_says == True:

            reset()

        elif user_says == False:

            print("Reset aborted.")

    else:

        print("Unknown command, file, or directory.")

def shutdown():

    print("Shutting Down...")

    raise SystemExit

def create_setup_file():

    try:

        with open("pydos_config.txt", "w") as file:

            print("Writing setup file...")

            file.write("do_setup = True")

            file.write("\nusername = None")

            print("Setup file successfully created.")

    except Exception as error:

        input(f"There was a problem with creating setup file. {error}")

print("CHECKING SETUP FILES...")

try:

    with open("pydos_config.txt", "r") as file:

        content = file.read()

        print(content)

        if "setup = True" in content:

            setup = True

        elif "setup = False" in content:

            setup = False

            if "username = None" not in content:

                code_to_run = content.replace("setup = False", "")

                code_to_run = content.replace("setup = True", "")

                exec(code_to_run)

                print(username)

except Exception as error:

    print(f"Could not read setup file. {error}")

    if error == "[Errno 2] No such file or directory: 'pydos_config.txt'":

        create_setup_file()

    else:

        create_setup_file()

try:

    if setup == True:

        input("Welcome to PY-DOS! Better known as the Python Disk Operating System. Press ENTER to continue.")

        username = input("Type in a name that you want the system to call you: ")

        with open("pydos_config.txt", "w") as file:

            file.write("do_setup = False")

            file.write(f"""\nusername = '{username}'""")

        setup = False

        input("Setup complete. Press ENTER to exit.")

except Exception as error:

    print("setup failed.")



input(f"Hello {username}, welcome to PY-DOS! Press ENTER to continue")

print("Type 'help' for help.")

while True:

    com_hub()

    try:

        if setup == True:

            input("Welcome to PY-DOS! Better known as the Python Disk Operating System. Press ENTER to continue.")

            username = input("Type in a name that you want the system to call you: ")

            with open("pydos_config.txt", "w") as file:

                file.write("do_setup = False")

                file.write(f"""\nusername = '{username}'""")

            input("Setup complete. Press ENTER to exit.")

        else:

            pass

    except Exception as error:

        print("setup failed.")