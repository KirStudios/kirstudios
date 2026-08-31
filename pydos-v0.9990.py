try:
    print("PYDOS 0.9990")
    global pydos_extend, pydosextend
    pydos_extend = False
    try:
        import pydosextend
        pydos_extend = True
    except BaseException:
        pydos_extend = False
    global pydos_logs
    pydos_logs = []

    global version
    version = 0.9990
    dev = "Kir Studios"
    #PY-DOS is made by Kir Studios
    dev_txt = f"PY-DOS is made by {dev}."
    print(dev)
    print(dev_txt)
    global ver
    if __name__ != "__main__":
        yeswarn = True
        external_program_path = ""

        try:
            raise Exception
        except Exception as e:
            frame = e.__traceback__.tb_frame
            
            while frame.f_back:
                frame = frame.f_back
                
            external_program_path = frame.f_code.co_filename

            with open(external_program_path, "r") as file:
                sus_source_code = file.read()
            with open(__file__, "r") as self_file:
                current_source = self_file.read()
  
        if external_program_path == __file__ and sus_source_code == current_source:
            connect = input(f"PY-DOS has executed another PY-DOS.")
            if connect == 'con':
                global pydoses_connect, pydos2nd
                pydoses_connect = True
                pydos2nd = current_source
            yeswarn = False
        if yeswarn == True:
            warn = input(f"PY-DOS has detected that it is running because another Python script or program imported or called PY-DOS to run it. If this isn't a false positive, then the progam may be able to collect any files or data stored in any variable or RAMdrive in this session, a major privacy risk. In order to reduce your chance of you creating data and it being stolen. You can shut down PY-DOS right now by pressing ENTER. Also, confirm that no other program is running PY-DOS, expect for the Python Interpreter, which is currently required to run this version of PY-DOS. If you belive this is a false postitive, then you can type 'norisk' then press ENTER.")
            if warn == 'norisk':
                print("You have continued into a risky state of PY-DOS. Make sure to know what you are doing and know that you can always shutdown PY-DOS. To shutdown PY-DOS, in Command Hub type 'shutdown' or type 'shutdown()' in a PY-DOS enviorment where you need to run Python code.")
            else:
                print("Shutting Down...")
                raise SystemExit
    print("Setting up system...")
    global recovery_env
    def recovery_env():
        print("--- Recovery Enviorment ---\n\n")
        print("Type 'exit recenv' to exit.\n")
        while True:
            code_to_exe = input("Type in Python code to execute: ")
            if code_to_exe == "exit recenv":
                break
            try:
                exec(code_to_exe)
            except Exception as code_error:
                print(code_error)

    def safe_recovery_env():
        print("--- Recovery Enviorment ---\n\n")
        print("Type 'exit recenv' to exit.\n")
        while True:
            badcoms = ['os.', 'sys.', 'subprocess.']
            code_to_exe = input("Type in Python code to execute: ")
            if code_to_exe == "exit recenv":
                break
            try:
                if any(cmd in code_to_exe.lower() for cmd in badcoms):
                    code_to_exe = "print('The Python code cannot be executed because it is considered a risk.')"
                    print("The Python code cannot be executed because it is considered a risk.")
                    continue
                exec(code_to_exe)
            except Exception as code_error:
                print(code_error)
    global no_config_file, verbal_dos, extra_protect, file_warn, ramdrive_allocate, ramdrive
    no_config_file = False
    verbal_dos = False
    #SETTING UP ALL OF THE FRICKING RAM DRIVESSS!
    ramdrive_ready = False
    first_time = False
    extra_protect = False
    calc_history = []
    file_warn = False
    ver = "PY-DOS 0.9990"
    pydos_application_developer_documentation = "Hello! Welcome to the PY-DOS Application Developer Documentation for versions 0.990 and higher!\n\n\nVariable Type Reminders:\n\nBOOL: TRUE or FALSE\n\nINT: A full number that contains no deciamls and only contains '0123456789'\n\nFLOAT: It can contain deciamls. For example, '123.123'\n\nSTR: Contains letters, and symbols, make sure to use INT for numbers or FLOAT for decimals or else most code will fail. But STR can contain numbers.\n\nCHAR: It stores ONLY and ONLY a single character. A character is like a single letter, number, or symbol. This currently (8/20/2026 as of typing this) does not exist in Python, every letter or symbol is stored as STR in Python. So you do not need to know CHAR unless you're reading this in the future and they added CHAR\n\\nnAPI Calls:\n\n'ramdrivemgr()' a function that allows you to rename (the command to this is 'ren'), edit (the command to this is 'edi'), delete (the command to this is 'del'), create (the command to this is 'cre'), or view (the command to this is 'vie') files in the RAMdrive. To type a command, type 'type=[the command you want to type]', 'filename=[input]', 'filecontent=[input]', 'edifilecontent=[input]', and 'renfilename=[input]'. These variables will be used when calling the function. This function can only be used when 'extra_protect' is FALSE.\n\n'confirm()' allows you to prompt the user. Just put the prompt inside the call, 'confirm(prompt=[input])'. The function will return a FALSE if the user says no, or a TRUE if the user says yes. You need to add extra logic to grab the return bool, and"
    ramdrive = {}
    current_drive = ramdrive
    current_drive_name = 'ramdrive'
    drives_allocate = {
        'ramdrive': 16,
    }
    drives_mapping = {
        'ramdrive': ramdrive

    }
    current_drive = ramdrive
    ramdrive_allocate = 16
    def reset():
        global setup, no_config_file
        try:
            with open("pydos_config.txt", "w") as file:
                print("Writing setup file...")
                file.write("do_setup = True")
                file.write("\nusername = '[]'")
                print("Setup file successfully created.")
                setup = True
        except Exception as error:
            input(f"There was a problem with creating setup file. {error}")
    def extrasafe():
        global file_warn, extra_protect
        file_warn = True
        extra_protect = True
    def drivemgr():
        global ramdrive, ramdrive_allocate, current_drive, drives_mapping, drives_allocate, output, addstr, itworks, blocked_keywords, blocked_characters, remcha
        while True:
            blocked_keywords = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
            blocked_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '~', '`']
            addstr = False
            output = False
            remcha = False
            itworks = None
            print(f"List of drives: {drives_mapping}")
            drivemgr_choice = input("Enter 0 to create a drive, enter 1 to delete a drive and move its contents, enter 2 to delete a drive and its contents, 3 to change the current drive, and enter 4 to exit Drive Manager: ")
            if drivemgr_choice == '0':
                prompt_user_for_name = True
                output = None
                while True:
                    breakloop = False
                    remcha = None
                    if prompt_user_for_name:
                        drivename = input("Enter the name of this new drive: ")
                        og_drivename = drivename
                    else:
                        print(drivename)
                    prompt_user_for_name = True
                    
                    if len(drivename) >= 17:
                        print("Drive name cannot be bigger than 16.")
                        continue

                    if drivename in blocked_keywords:
                        makelog("Drive name cannot only contain a Python reserved word.", 1)
                        addstr = confirm("Would you like to add a word at the start so it's no longer a Python reserved word?")
                        if addstr == False:
                            prompt_user_for_name = True
                            continue

                    for char in blocked_characters:
                        if char in drivename:
                            makelog("Drive name cannot contain a Python reserved character.", 1)
                            remcha = confirm("Would you like to remove the reserved character so it no longer has a Python reserved character?")
                            if remcha == False:
                                break
                    if addstr == True:
                        pass

                    if remcha == False:
                        continue

                    if remcha == True:
                        for char in blocked_characters:
                            drivename = drivename.replace(char, "")
                        print(f"Your drive name has been changed from '{og_drivename}' to '{drivename}' in order to comply with drive naming rules.")
                        prompt_user_for_name = False
                                            
                    if " " in drivename: 
                        print("Drive name cannot contain spaces.")
                        output = confirm("Would you like to replace the spaces with underscores? From ' ' to '_'?")
                        if output == True:
                            drivename = drivename.replace(" ", "_")
                            prompt_user_for_name = False
                            output = None  # Reset output
                        else:
                            continue

                    try:
                        float(drivename)
                        makelog("Drive names must contain at least 1 letter.", 1)
                        addstr = confirm("Would you like to add a word at the start so it has a letter?")
                        if addstr == False:
                            makelog("Drive names must contain at least 1 letter.", 2)
                            continue
                    except:
                        pass

                    if addstr == False:

                        ints = '0', '1', '2', '3', '4', '5', '6', '7', '8','9'
                        starts_with_num = False
                        for integer_digit in ints:
                            if drivename.startswith(integer_digit):
                                starts_with_num = True
                                break
                        if starts_with_num:
                            makelog("Drive name cannot start with a number.", 1)
                            addstr = confirm("Would you like to add a word at the start so it starts with a letter?")
                            if addstr == False:
                                makelog("Drive name must contain at least 1 letter.", 2)
                                continue

                    if addstr == True:
                        #tries to add a word to the drive name
                        words = ['drive', 'dri', 'd']
                        itworks = False
                        for word in words:
                            prompt_user_for_name = False
                            og_drivename = drivename
                            drivename = f"{word}{drivename}"
                            if len(drivename) <= 16:
                                print(f"Your drive name has been changed from '{og_drivename}' to '{drivename}' in order to comply with drive naming rules.")
                                itworks = True
                                break
                            elif len(drivename) >= 17:
                                drivename = og_drivename
                                itworks = False
                    if itworks == False:
                        print("Unable to apply word at front because there isn't enough character space to do so.")
                        continue

                    breakloop = True

                    if breakloop:
                        break

                while True:
                    try:
                        driveallocate = input("Allocate this drive (default is 16 if you don't enter anything): ")
                        print("Creating drive...")
                        if driveallocate == '':
                            driveallocate = 16
                        int(driveallocate)
                        exec(f"global drives_allocate, driveallocate, drivename, drives_mapping, {drivename}; {drivename} = {{}}; drives_allocate['{drivename}'] = {driveallocate}; drives_mapping['{drivename}'] = {drivename}")
                        print("Drive created.")
                        break
                    except KeyboardInterrupt:
                        break
                    except Exception as err:
                        makelog(f"There was a problem while attempting to create drive. {err}", 1)
                        continue
            elif drivemgr_choice == '1':
                print("Feature not here yet.")
            elif drivemgr_choice == '2':
                print("Feature not here yet.")
            elif drivemgr_choice == '3':
                desired_drive = input("Enter the drive name you want to switch to: ")
                if desired_drive in drives_mapping:
                    current_drive = drives_mapping[desired_drive]
                    current_drive_name = desired_drive
                    print(f"Switched to {desired_drive}")
                else:
                    print(f"The drive '{desired_drive}' could not be found")
            elif drivemgr_choice == '4':
                print("Exiting Drive Manager...")
                break
    def checkramdrive():
        global ramdrive, ramdrive_allocate, current_drive, current_drive_name
        if ramdrive_allocate < 0:
            input(f"FATAL MISMATCH! Detected fatal mismatch in RAMdrive. RAMdrive is allocated to use {ramdrive_allocate}! It is a negative number! Which is impossible! RAMdrive allocation WILL increase to 0 when you press ENTER.")
            ramdrive_allocate = 0
            return
        if len("".join([f"{k}{v}" for k, v in current_drive.items()])) > ramdrive_allocate:
            wipe = input(f"FATAL MISMATCH! Detected fatal mismatch in RAMdrive. RAMdrive is currently using {len("".join([f"{k}{v}" for k, v in current_drive.items()]))} of space, while the RAMdrive is allocated to only use {ramdrive_allocate}. For this reason, the RAMdrive will now be wiped when you press ENTER. To avoid losing files, type 'nowipe' then ENTER.")
            if wipe == 'nowipe':
                old_ramdrive_allocate = ramdrive_allocate
                ramdrive_allocate = len("".join([f"{k}{v}" for k, v in current_drive.items()]))
                print(f"Full RAMdrive wipe has been aborted. Allocation size increased from {old_ramdrive_allocate} to {ramdrive_allocate} to support larger files insetad of fully wiping the RAMdrive.")
                return
            if wipe == 'helprec':
                print("Help message detected! You are now safeley in Command Hub!")
                while True: com_hub()
            ramdrive = {}
            current_drive_name = 'ramdrive'
            print("RAMdrive has been fully wiped.")

    #NON-SYSTEM FUNCTIONS <--
    def calc(op=None, n1=None, n2=None):
        try:
            n1 = float(n1)
            n2 = float(n2)
            op = str(op)
        except Exception as err:
            print(f"The expression could not be completed. One or more variables given is not the expected type. {err}")
            return
        if op == '/':
            res = n1 / n2
        elif op == '+':
            res = n1 + n2
        elif op == '-':
            res = n1 - n2
        elif op == '*':
            res = n1 * n2
        return res

    def makelog(log=None, type=0):
        if log == None:
            return
        if type == 2:
            print(log)
            return
        try:
            raise Exception
        except Exception as e:
            tb = e.__traceback__
                    
            if tb and tb.tb_frame and tb.tb_frame.f_back:
                caller_frame = tb.tb_frame.f_back
                caller_name = caller_frame.f_code.co_name
            else:
                caller_name = '-UNKNOWN-'
        pydos_logs.append(f"[{caller_name}]{log}")
        if type == 1:
            print(log)
    #-->
    def changeramdriveallocate(newallocate=16):
        global ramdrive_allocate
        oldallocate = ramdrive_allocate
        ramdrive_allocate = newallocate
        print(f"The RAMdrive allocation has been changed from {oldallocate} to {ramdrive_allocate}. If this allocation is too big for your system, you can use a function said in the PY-DOS App Dev Doc.")
    def ramdriveinfo():
        global drives_allocate, drives_mapping
        total_files_across_drives = 0
        for drives in drives_mapping:
            dir = drives_mapping[drives]
            add = len(dir.values())
            total_files_across_drives = total_files_across_drives + add

        info = f"Total Drives: {len(drives_mapping)}\nTotal Files: {total_files_across_drives}\n"

        for drive_name in drives_mapping:
            drive_dict = drives_mapping[drive_name] 
            used_space = len("".join([f"{k}{v}" for k, v in drive_dict.items()]))
            allocated = drives_allocate[drive_name]
            free_space = allocated - used_space
            total_files = len(drives_mapping[drive_name])
            info = f"{info}{drive_name}:\n  Total Files: {total_files}\n  Total Space: {allocated}\n  Used Space: {used_space}\n  Free Space: {free_space}\n\n"
        print(info)
        return info
    def confirm(prompt):
        global username, temp_username
        while True:
            response = input(f"{prompt} (y/n): ")
            if response in ["yess", "yes", "y", "ye"]:
                return True
            elif response in ["noo", "no", "n"]:
                return False
            else:
                print("That's not a valid respone.")
    def ramdrivemgr(type=None, filename=None, renfilename=None, filecontent=None, edifilecontent=None, origin='.UNKNOWN.'):
        checkramdrive()
        global extra_protect, file_warn
        safecallers = ['com_hub', 'ramdrivemgr', 'confirm', 'reset', 'shutdown']
        try:
            raise Exception
        except Exception as e:
            tb = e.__traceback__
            
            if tb and tb.tb_frame and tb.tb_frame.f_back:
                caller_frame = tb.tb_frame.f_back
                caller_name = caller_frame.f_code.co_name
            else:
                caller_name = '.UNKNOWN.'

        claimed_caller_name = origin 

        if claimed_caller_name is None:
            claimed_caller_name = '.UNKNOWN.'
        if claimed_caller_name != caller_name:
            if extra_protect:
                print(f"EXTRA PROTECT: Mismatch detected! Caller said it was '{claimed_caller_name}' while it's true name is '{caller_name}'. Since Extra Protect is on. RAMdrive Manager will now refuse to do anything and will now return.")
                return

        if extra_protect:
            if caller_name not in safecallers:
                print(f"EXTRA PROTECT: The true caller name wasn't in the safe caller list! Since Extra Protect is on. RAMdrive Manager will now refuse to do anything and will now return.")
                return
        print(f"I was called by '{caller_name}'.")
        print(f"I was told that I was called by '{claimed_caller_name}'.")

        if type == 'del':
            if filename not in current_drive:
                print(f"Unable to delete, '{filename}' because it does not exist on the RAMdrive.")
                return
            if not file_warn:
                del current_drive[filename]
                print("File deleted.")
            elif file_warn:
                user_says = confirm(f"Are you sure you want to delete the file, '{filename}'?")
                if user_says == True:
                    del current_drive[filename]
                    print("File deleted.")
                elif user_says == False:
                    print("File deletion aborted.")
        elif type == 'cre':
            current_drive[filename] = filecontent
            print("File created.")
        elif type == 'edi':
            if filename not in ramdrive:
                print(f"Unable to edit, '{filename}' because it does not exist on the RAMdrive.")
                return
            del current_drive[filename]
            current_drive[filename] = edifilecontent
            print("File edited.")
        elif type == 'ren':
            if filename not in ramdrive:
                print(f"Unable to rename, '{filename}' because it does not exist on the RAMdrive.")
                return
            temp_filecontent = current_drive[filename]
            del current_drive[filename]
            current_drive[renfilename] = temp_filecontent
            print("File renamed.")
        elif type == 'vie':
            if filename not in ramdrive:
                print(f"Unable to view, '{filename}' because it does not exist on the RAMdrive.")
                return
            print(current_drive[filename])
        else:
            print("Unknown command type from call. (RAMdrive Manager)")

    #OPENING THE GOD DAMN FILES!

    def autorun_code():
        print("Automatically executing your stored Python code...")
        try:
            with open("pydos_autorun.txt", "r") as file:
                content = file.read()
                exec(content)
        except FileNotFoundError as error:
            makelog(f"Automatic autorun executing has failed. You can try to execute your stored Python code from the autorun file by typing 'exestoredpy' when you get to the Command Hub. Error: {error}", 0)
            return
        except Exception as error:
            makelog(f"Automatic autorun executing has failed. You can try to execute your stored Python code from the autorun file by typing 'exestoredpy' when you get to the Command Hub. Error: {error}", 1)
        
    def load_imports_auto():
        print("Automatically loading your stored imports...")
        global imports
        imports = []
        try:
            with open("pydos_imports.txt", "r") as file:
                code = file.read()
                code = f"global imports\n{code}"
                exec(code)
                for import_item in imports:
                    globals() [import_item] = __import__(import_item)
                    print(f"Loaded in '{import_item}' module...")
        except FileNotFoundError as error:
            makelog(f"Automatic import loading has failed. You can try to load imports from the imports file by typing 'loadimports' when you get to the Command Hub. Error: {error}", 0)
            return
        except Exception as error:
            makelog(f"Automatic import loading has failed. You can try to load imports from the imports file by typing 'loadimports' when you get to the Command Hub. Error: {error}", 1)
    def readpydrive():
        try:
            global drives_mapping, drives_allocate, ramdrive
            print("Loading files from PyDrive...")
            with open("pydos_pydrive.txt", "r") as file:
                pydrive = file.read()
                pydrive = f"global drives_mapping, drives_allocate, ramdrive\n{pydrive}"
                exec(pydrive)
            print("Successfully loaded files from PyDrive...")
        except FileNotFoundError as err:
            makelog(f"There was an issue while trying to edit or create the PyDrive. {err}", 0)
        except Exception as err:
            makelog(f"There was an issue while trying to edit or create the PyDrive. {err}", 1)
    def savepydrive():
        try:
            global drives_mapping, drives_allocate, ramdrive
            print("Saving your drives and files to PyDrive...")
            with open("pydos_pydrive.txt", "w") as file:
                file.write(f"drives_mapping = {drives_mapping}\n")
                file.write(f"drives_allocate = {drives_allocate}\n")
                for saving_drive in drives_mapping.keys():
                    file.write(f"{saving_drive} = {drives_mapping[saving_drive]}\n")
            print("PyDrive succcessfully created.")
        except FileNotFoundError as err:
            makelog(f"There was an issue while trying to edit or create the PyDrive. {err}", 0)
        except Exception as err:
            makelog(f"There was an issue while trying to edit or create the PyDrive. {err}", 1)
    def com_hub(command=None):
        checkramdrive()
        global no_config_file, username, temp_username
        commands = ['help', 'shutdown', 'username', 'editname', 'pyfile', 'executefile', 'safeexecutefile', 'execute', 'safeexecute', 'say', 'reset', 'ver', 'recenv', 'imports', 'loadimports', 'listimports', 'autorun', 'exestoredpy', 'drivemgr', 'createfile', 'editfile', 'delete', 'viewfile', 'deletefile', 'renamefile', 'viewramdrive', 'syncpydrive', 'currentdrive', 'calc', 'exitcom']
        if command == None:
            command = input("Type Command: ")
        if command == 'help':
            com_hub_help = f"All Commands:\n\n-Power Modes-\n\nshutdown - turns off computer\n\n-Username Commands-\n\nusername - the terminal will say your current username\neditname - edits your username\n\n-Factory Reseting-\n\nreset - resets this computer\n\n-PY-DOS Tools-\n\nsay [input] - the terminal will repeat what you said\ncalc - calculates math expressions\n\n-Run Python Code-\n\nexecute [input] - runs the Python code in [input]\nexecute - asks you what Python code to run\nsafeexecute [input] - runs the Python code in [input] safely\nsafeexecute - asks you what Python code to run safely\nexecutefile - lets you execute a file if it stores Python code\nsafeexecutefile - lets you execute a file if it stores Python code\npyfile - lets you execute a real file if it stores Python code\n\n-Information-\n\nver - tells you your current PY-DOS version\n\n-Imports & Importing-\n\nimports - opens the Import Manager\nloadimports - loads imports on command\nlistimports - view all of the modules stored in the config file as a raw list\n\n-Auto Running Python Code-\n\nautorun - lets you create a file with Python code so when you start up PY-DOS, it auto reads the file and executes the code in that file\nexestoredpy - reads the autorun file and exeuctes the Python code you have in that file\n\n-RAMdrive Managing-\n\ndrivemgr - lets you manage drives\ncreatefile - create a file on the RAMdrive\neditfile - edits a file on the RAMdrvive\nviewfile - view the content of a file on the RAMdrive\nviewramdrive - view the entire RAMdrive and every single item on it in raw format.\ndeletefile - deletes the file on the RAMdrive\nrenamefile - lets you rename a file on the RAMdrive.\n[input] - lets you see if a file exists by typing the filename\nsyncpydrive - saves all of your drives and files to the PyDrive\ncurrentdrive - tells you the current drive\n\n-Recovery Options-\n\nrecenv - brings you into the recovery enviorment\nexitcom - exit Command Hub\n\n\nYou are using {ver}. {dev_txt}"
            print(com_hub_help)
        elif command == 'shutdown':
            user_says = confirm("Are you sure? Any unsaved work will be lost.")
            if user_says == True:
                shutdown()
            elif user_says == False:
                print("Shutdown aborted.")
        elif command == 'username':
            print(username)
        elif command == 'editname':
            temp_username = input("Type in your new username: ")
            user_says = confirm(f"Are you sure you want to change your username from '{username}' to '{temp_username}'?")
            print("Changing username...")
            if user_says == True:
                if no_config_file == False:
                    try:
                        with open("pydos_config.txt", "w") as file:
                            print("Writing setup file...")
                            file.write("do_setup = False")
                            file.write(f"\nusername = '{temp_username}'")
                            print("Setup file successfully changed.")
                    except Exception as error:
                        input(f"There was a problem with changing username. {error}")
                username = temp_username
                print("Username changed.")
            elif user_says == False:
                print("Username change aborted.")
        elif command == 'pyfile':
            file = input("What file in your computer should PY-DOS execute?: ")
            with open(file, 'r') as file2:
                exe = file2.read()
                exec(exe)
        elif command == 'executefile':
            exe_filename = input("Type in the filename of the file you want to execute: ")
            try:
                exec(current_drive[exe_filename])
            except Exception as error:
                print(error)
        elif command == 'safeexecutefile':
            exe_filename = input("Type in the filename of the file you want to execute safely: ")
            try:
                exec(current_drive[exe_filename])
            except BaseException as error:
                print(error)
        elif command[:7] == 'execute':
            temp_command = command.replace(" ", "")
            if temp_command == "execute":
                temp_code = input("Type in Python code to execute: ")
            else:
                temp_command_2 = command.replace(" ", "!@#$%^&*()")
                if temp_command_2.startswith("execute!@#$%^&*()"):
                    temp_code = command[8:]
                else:
                    temp_code = command[7:]
            user_says = confirm(f"Are you sure you want to run this Python code?")
            if user_says == True:
                print("Executing...")
                try:
                    exec(temp_code)
                except Exception as code_error:
                    print(code_error)
                print("Finished execution.")
            elif user_says == False:
                print("Python code execution aborted.")
        elif command[:11] == 'safeexecute':
            temp_command = command.replace(" ", "")
            if temp_command == "safeexecute":
                temp_code = input("Type in Python code to execute safely: ")
            else:
                temp_command_2 = command.replace(" ", "!@#$%^&*()")
                if temp_command_2.startswith("safeexecute!@#$%^&*()"):
                    temp_code = command[12:]
                else:
                    temp_code = command[11:]
            user_says = confirm(f"Are you sure you want to run this Python code?")
            if user_says == True:
                print("Executing...")
                try:
                    exec(temp_code)
                except BaseException as code_error:
                    print(code_error)
                print("Finished execution.")
            elif user_says == False:
                print("Python code execution aborted.")
        elif command[:3] == 'say':
            temp_command_2 = command.replace(" ", "")
            if command.startswith("say "):
                what_to_say = command[4:]
                print(what_to_say)
            else:
                what_to_say = command[3:]
                print(what_to_say)
        elif command == 'reset':
            if no_config_file == True:
                print("This command cannot be executed in No Configuration File mode.")
                return
            user_says = confirm("Are you sure you want to reset this computer? By resetting, you delete all data from this computer and bring PY-DOS back to setup.")
            if user_says == True:
                reset()
            elif user_says == False:
                print("Reset aborted.")
        elif command == 'ver':
            print(ver)
        elif command == 'recenv':
            user_says = confirm("Are you sure you want to enter into recovery enviorment?")
            if user_says == True:
                recovery_env()
            elif user_says == False:
                print("Recovery enviorment aborted.")
        elif command == 'imports':
            print("\nWelcome to Import Manager! Where you can type in the names of modules that you want PY-DOS to automatically load in when you start it from the 'pydos_config.txt' file.\n\n")
            print("Type ':exit:' to leave.")
            print("Type ':remove:[input]' with no spaces in bewteen to remove a module from the list.")
            print("Type ':list:' to view the list.")
            imports_to_auto_load = []
            while True:
                add_import = input("Type in the name of a module you want to auto load: ")
                if add_import == ":exit:":
                    break
                elif ":remove:" in add_import:
                    what_to_remove = add_import.replace(":remove:", "")
                    imports_to_auto_load.remove(what_to_remove)
                    print(f"The module '{what_to_remove}' has been removed.")
                elif add_import == ":list:":
                    print(imports_to_auto_load)
                else:
                    imports_to_auto_load.append(add_import)
                    print(f"The module, '{add_import}' has been successfully added to the list, ready to save when you exit.")
            try:
                with open("pydos_imports.txt", "w") as file:
                    print("Writing import file...")
                    file.write(f"imports = {imports_to_auto_load}")
                    print("Import file successfully created.")
            except Exception as error:
                input(f"There was a problem with creating Import file. {error}")
        elif command == 'loadimports':
            load_imports_auto()
        elif command == 'listimports':
            print(imports)
        elif command == 'autorun':
            code = input("Type Python code you want to run every single time you start up PY-DOS: ")
            try:
                with open("pydos_autorun.txt", "w") as file:
                    print("Writing autorun file...")
                    file.write(code)
                    print("Autorun file successfully created.")
            except Exception as error:
                input(f"There was a problem with creating Import file. {error}")
        elif command == 'exestoredpy':
            autorun_code()
        #managing ram drive (ramcom)
        elif command == 'drivemgr':
            drivemgr()
        elif command == 'createfile':
            com_filename = input("Type in filename (include file format too): ")
            com_filecontent = input("Type in the file content: ")
            space_used = len(com_filename) + len(com_filecontent)
            if len("".join([f"{k}{v}" for k, v in current_drive.items()])) + space_used > ramdrive_allocate:
                print(f"There isn't enough space in the RAMdrive to manage this file.\nTotal Space: {ramdrive_allocate}\nUsed Space: {len("".join([f"{k}{v}" for k, v in current_drive.items()]))}\nFree Space: {ramdrive_allocate - len("".join([f"{k}{v}" for k, v in current_drive.items()]))}\nFree Space Needed To Manage File: {space_used}")
                return
            current_drive[com_filename] = com_filecontent
            print("File created.")
            print(f"Drive: {current_drive_name}\nTotal Space: {ramdrive_allocate}\nUsed Space: {len("".join([f"{k}{v}" for k, v in current_drive.items()]))}\nFree Space: {ramdrive_allocate - len("".join([f"{k}{v}" for k, v in current_drive.items()]))}")
        elif command == 'editfile':
            com_edit_filename = input("Type in filename (include file format too): ")
            com_filecontent = input("Type in the new file content: ")
            space_used = len(com_edit_filename) + len(com_filecontent)
            if len("".join([f"{k}{v}" for k, v in current_drive.items()])) + space_used > ramdrive_allocate:
                print(f"There isn't enough space in the RAMdrive to manage this file.\nTotal Space: {ramdrive_allocate}\nUsed Space: {len("".join([f"{k}{v}" for k, v in current_drive.items()]))}\nFree Space: {ramdrive_allocate - len("".join([f"{k}{v}" for k, v in current_drive.items()]))}\nFree Space Needed To Manage File: {space_used}")
                return
            user_says = confirm(f"Are you sure you want to edit the file, '{com_edit_filename}'? The content will change from '{current_drive[com_edit_filename]}' to '{com_filecontent}'")
            if user_says == True:
                del current_drive[com_edit_filename]
                current_drive[com_edit_filename] = com_filecontent
                print("File edited.")
            elif user_says == False:
                print("File editing aborted.")
        elif command == 'viewfile':
            view_filename = input("Type in the filename (include the file format): ")
            print(current_drive[view_filename])
        elif command[:8] == 'viewfile':
            temp_command_3 = command.replace(" ", "")
            if command.startswith("viewfile "):
                view_filename = command[9:]
                print(current_drive[view_filename])
            else:
                view_filename = command[8:]
                print(current_drive[view_filename])
        elif command == 'deletefile':
            com_del_filename = input("Type in the filename (include the file format): ")
            user_says = confirm(f"Are you sure you want to delete the file, '{com_del_filename}'?")
            if user_says == True:
                del current_drive[com_del_filename]
                print("File deleted.")
            elif user_says == False:
                print("File deletion aborted.")
        elif command == 'renamefile':
            com_to_edit_filename = input("Type in the filename you want to rename (include the file format): ")
            com_edit_filename = input("Type in the new filename (include the file format): ")
            space_used = len(com_to_edit_filename) + len(com_edit_filename)
            if len("".join([f"{k}{v}" for k, v in current_drive.items()])) + space_used > ramdrive_allocate:
                print(f"There isn't enough space in the RAMdrive to manage this file.\nTotal Space: {ramdrive_allocate}\nUsed Space: {len("".join([f"{k}{v}" for k, v in current_drive.items()]))}\nFree Space: {ramdrive_allocate - len("".join([f"{k}{v}" for k, v in current_drive.items()]))}\nFree Space Needed To Manage File: {space_used}")
                return
            temp_com_edit_filecontent = current_drive[com_to_edit_filename]
            del current_drive[com_to_edit_filename]
            current_drive[com_edit_filename] = temp_com_edit_filecontent
            print("File renamed.")
        elif command == 'viewramdrive':
            print(ramdrive)
        elif command == 'syncpydrive':
            savepydrive()
        elif command == 'currentdrive':
            print(f"The drive you are using to create, edit, delete, and view files is '{current_drive_name}'.")
        elif command == 'calc':
            show_err = False
            view_calc_history = confirm("Do you want to view your calculation histroy? Type 'n' to calculate instead")
            if view_calc_history == True:
                print("Remember, + is addition, - is subtraction, / is division, and * is multiplication")
                print(calc_history)
                return
            elif view_calc_history == False:
                pass
            while True:
                try:
                    num1 = input("Type the first number: ")
                    num1 = int(num1)
                    break
                except Exception as err:
                    try:
                        num1 = float(num1)
                    except:
                        show_err = True
                        pass
                    if show_err:
                        makelog(f"Please type a number. If you did, an error has happened. {err}", 1)
                    if not show_err:
                        break
            while True:
                try:
                    num2 = input("Type the second number: ")
                    num2 = int(num2)
                    break
                except Exception as err:
                    try:
                        num2 = float(num2)
                    except:
                        show_err = True
                        pass
                    if show_err:
                        makelog(f"Please type a number. If you did, an error has happened. {err}", 1)
                    if not show_err:
                        break
            while True:
                type = input("What is the operator type? (0 for addition, 1 for subtraction, 2 for division, and 3 for multiplication): ")
                if type == '0':
                    res = num1 + num2
                    ope = '+'
                    break
                elif type == '1':
                    res = num1 - num2
                    ope = '-'
                    break
                elif type == '2':
                    res = num1 / num2
                    ope = '/'
                    break
                elif type == '3':
                    res = num1 * num2
                    ope = '*'
                    break
                else:
                    print("Please type a valid option.")
            equation = f"{num1} {ope} {num2} = {res}"
            calc_history.append(equation)
            print(f"The result is {res}")
        elif command == 'exitcom':
            print("Exiting Command Hub...")
            return
        elif command in current_drive and '.' in command:
            print(f"The file '{command}' does exist.")
        elif command not in current_drive and '.' in command:
            print(f"The file '{command}' does not exist.")
        else:
            print(f"Unknown command, file, or drive.")
            try:
                if pydos_extend:
                    import pydosextend
                    output = pydosextend.do("unknowncom", command, commands)
                    if "'None'" not in output:
                        print(output)
            except Exception as err:
                makelog(f"A problem has happened with PY-DOS Extend. {err}", 0)
    def shutdown():
        print("Shutting Down...")
        raise SystemExit

    def confirm_shutdown():
        user_says = confirm("Are you sure you want to shutdown? Any unsaved work will be lost.")
        if user_says == True:
            shutdown()
        elif user_says == False:
            print("Shutdown aborted.")
    
    #<-- SETUP LOGIC AND STUFF -->

    def create_setup_file():
        global no_config_file, setup
        try:
            with open("pydos_config.txt", "w") as file:
                print("Writing setup file...")
                file.write("do_setup = True")
                file.write("\nusername = None")
                print("Setup file successfully created.")
                setup = True
        except Exception as error:
            input(f"There was a problem with creating setup file. {error}")
            user_says = confirm("Do you want to run PY-DOS into No Configuration File mode?")
            if user_says == True:
                no_config_file = True
            elif user_says == False:
                pass
                fatal_error_input = input("PY-DOS will now shutdown once you press ENTER. (Or type 'recenv' to enter recovery enviroment)")
                if fatal_error_input == 'recenv':
                    recovery_env()
                else:
                    shutdown()
    if no_config_file == False:
        print("CHECKING SETUP FILES...")
        try:
            with open("pydos_config.txt", "r") as file:
                content = file.read()
                if "do_setup = True" in content: 
                    setup = True
                elif "do_setup = False" in content: 
                    setup = False
                    if "username = None" not in content:
                        code_to_run = content.replace("do_setup = False", "")
                        code_to_run = content.replace("do_setup = True", "")
                        exec(code_to_run)
        except Exception as error:
            makelog(f"Could not read setup file. {error}", 1)
            setup = False
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
            makelog(f"Setup failed. Error: {error}", 1)
    else:
        setup = False
        username = "Temp_User"
    if no_config_file == True:
        setup = False
        username = "Temp_User"
    autorun_code()
    load_imports_auto()
    readpydrive()
    input(f"Hello {username}, welcome to PY-DOS! Press ENTER to continue")
    print("Type 'help' for help.")
    while True:
        try:
            checkramdrive()
            com_hub()
            if no_config_file == False:
                try:
                    if setup == True and no_config_file == False:
                        input("Welcome to PY-DOS! Better known as the Python Disk Operating System. Press ENTER to continue.")
                        username = input("Type in a name that you want the system to call you: ")
                        with open("pydos_config.txt", "w") as file:
                            file.write("do_setup = False")
                            file.write(f"""\nusername = '{username}'""")
                        setup = False
                        input("Setup complete. Press ENTER to exit.")
                    else:
                        pass
                except Exception as error:
                    makelog(f"Setup failed. {error}", 1)
        except KeyboardInterrupt:
            confirm_shutdown()
            continue
except KeyboardInterrupt:
    shutdown()
except Exception as e:
    try:
        crash = input(f"PYDOS has crashed. When you press ENTER, the system will now shut down. To enter recovery enviorment, type 'recenv' then press ENTER. Error Code: {e}")
        if crash != "recenv":
            raise SystemExit
        else:
            recovery_env()
        raise SystemExit
    except Exception as e2:
        input(e2)
        raise SystemExit