#this is for testing, please remove this block once released ->
debug = False
if debug:
    print2 = print
    input2 = input
    def input(msg):
        import time
        return input2(f"{msg} {time.time()}")
    def print(msg=None):
        if msg == None:
            msg = ''
        import time
        print2(msg, time.time())
#<-
if debug:
    print("PY-DOS Extend is running. No thread is active yet so PY-DOS Extend has main thread-executon control.")
try:
    dev = "Kir Studios"
    mainapp = "PY-DOS"
    #BOTH PY-DOS AND PY-DOS EXTEND ARE MADE BY KIR STUDIOS
    if __name__ == "__main__":
        input("Hi! Welcome to PY-DOS Extend! So glad you have installed this PY-DOS Application, but this PY-DOS Application requires you to run it in PY-DOS. Press ENTER to exit.")
        raise SystemExit
    global modules_made, pydos_extend_logs, savepydrive, version
    modules_made = False
    import threading
    global uptime
    global keepcounting
    keepcounting = True
    if debug:
        print("Defining uptime counter thread...")
    def countuptime():
        import time
        global uptime
        global keepcounting
        uptime = 0
        while True:
            time.sleep(1)
            uptime = uptime + 1
    if debug:
        print("Running uptime counter...")
    uptimecounter = threading.Thread(target=countuptime)
    uptimecounter.daemon = True
    uptimecounter.start()
    if debug:
        print("Defining background task thread...")
    def turnonmaid(v0=None, v1=None, v2=None, v3=None, v4=None, v5=None, v6=None, v7=None, v8=None, v9=None, v10=None):
        import threading
        def nouserneededbackgroundtaskmanager(v2):
            import time
            import random
            global version
            global compose
            while True:
                #50, 200
                time.sleep(random.uniform(50, 200))
                #ACTION 1: CHECK FOR UPDATES
                if v2 > 0:
                    result = do(com='silentupdate', s1=v0)
                    v1('Background Update Check Status Complete!', result[0], 'PY-DOS Extend')
                else:
                    v1('Unable to scan for updates.', 'PY-DOS cannot scan for updates because PY-DOS ran out of network tokens. You can set more by increasing "network_tokens" value to 1 or higher.', 'PY-DOS Extend')
                v2 -= 1 # Fixed from =- to -=
                #ACTION 2: LET USER KNOW UPTIME
                if random.randint(0, 3) == 2:
                    v1('Uptime Info', f'The Current Uptime For This PY-DOS Session Is {do(com='getpydosuptime')} Seconds.', 'PY-DOS Extend')
                #9, 20
                time.sleep(random.uniform(9, 20))
        global maidthread
        # Added parenthesis and a trailing comma to force a tuple format
        maidthread = threading.Thread(target=nouserneededbackgroundtaskmanager, args=(v2,))
        maidthread.daemon = True
        maidthread.start()
    if debug:
        print("Defining other functions for PY-DOS Extend...")

    pydos_extend_logs = []
    #WHAT PY-DOS CALLS TO DO
    def do(com=None, s1=None, s2=None, s3=None, s4=None, s5=None):
        try:
            global pydocommand, commands
            #USER TYPES UNKNOWN COMMAND
            if com == 'unknowncom':
                from thefuzz import process
                #Default is 80, Strict is 90. and Loosey is 70. The last two modes will be added in later builds of Extend.
                fuzz_per = 80

                result = process.extractOne(s1, s2)

                if result and result[1] >= fuzz_per:
                    best_match = result[0]
                else:
                    best_match = None

                output = f"Perhaps you meant to type '{best_match}'?"
                if 'backuppydrive' in s2 or s3 >= 0.9997:
                    return output, best_match
                else:
                    return output

            #CONTACTS GITHUB SERVERS TO FIND A NEW PY-DOS VERSION
            elif com == 'update':
                import requests
                print("Checking for newer versions...")
                repo_owner = "KirStudios"
                repo_name = "kirstudios"
                api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents"

                print("Contacting server...")
                response = requests.get(api_url)

                if response.status_code == 200:
                    items = response.json()
                    print("Successfully got a list of hosted versions. Comparing them to this session's version...")
                    
                    pydos_vers = []
                    for item in items:
                        filename = item['name']
                        if filename.startswith("pydos-v") and filename.endswith(".py"):
                            ver_str = filename.replace("pydos-v", "").replace(".py", "")
                            try:
                                pydos_vers.append(float(ver_str))
                            except ValueError:
                                pass
                    
                    version = float(s1)
                    print(f"All hosted versions: {pydos_vers}")
                    print(f"Current installed version: {version}")
                    
                    if pydos_vers:
                        if version >= max(pydos_vers):
                            if version > max(pydos_vers):
                                print("Your PY-DOS version is a build not uploaded or deleted from GitHub! Take good care of it! Your PY-DOS version is up to date!")
                                return
                            print("Your PY-DOS version is up to date! :D")
                        else:
                            print("[!] Your PY-DOS version is not up to date [!]")
                    else:
                        print("No valid version files found on server.")
                else:
                    print(f"Failed to fetch repository contents: {response.status_code}")
            #SILENT UPDATE
            elif com == 'silentupdate':
                import requests
                repo_owner = "KirStudios"
                repo_name = "kirstudios"
                api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents"
                response = requests.get(api_url)
                if response.status_code == 200:
                    items = response.json()                    
                    pydos_vers = []
                    for item in items:
                        filename = item['name']
                        if filename.startswith("pydos-v") and filename.endswith(".py"):
                            ver_str = filename.replace("pydos-v", "").replace(".py", "")
                            try:
                                pydos_vers.append(float(ver_str))
                            except ValueError:
                                pass
                    
                    version = float(s1)
                    
                    if pydos_vers:
                        if version >= max(pydos_vers):
                            if version > max(pydos_vers):
                                return "Your PY-DOS version is a build not uploaded or deleted from GitHub! Take good care of it! Your PY-DOS version is up to date!", 0
                            return "Your PY-DOS version is up to date! :D", 1
                        else:
                            return "[!] Your PY-DOS version is not up to date [!]", 2
                    else:
                        return "No valid version files found on server for update checking", 3
                else:
                    return f"Failed to fetch repository contents for update checking: {response.status_code}", 4




            #INSTALLS THE UPDATE!
            elif com == 'installupdate':
                print("Checking for newer versions...")
                import requests
                import requests
                repo_owner = "KirStudios"
                repo_name = "kirstudios"
                api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents"

                print("Contacting server...")
                response = requests.get(api_url)

                if response.status_code == 200:
                    items = response.json()
                    print("Successfully got a list of hosted versions. Comparing them to this session's version...")
                    
                    pydos_vers = []
                    for item in items:
                        filename = item['name']
                        if filename.startswith("pydos-v") and filename.endswith(".py"):
                            ver_str = filename.replace("pydos-v", "").replace(".py", "")
                            try:
                                pydos_vers.append(float(ver_str))
                            except ValueError:
                                pass
                    
                    version = float(s1)
                    print(f"All hosted versions: {pydos_vers}")
                    print(f"Current installed version: {version}")
                    if version >= max(pydos_vers):
                        if version > max(pydos_vers):
                            print("Your PY-DOS version is a build not uploaded or deleted from GitHub! Take good care of it! Your PY-DOS version is up to date!")
                            return
                        print("Your PY-DOS version is up to date!")
                    else:
                        print("Your PY-DOS version is not up to date [!]")
                else:
                    print(f"Failed to fetch repository contents: {response.status_code}")
                    
                import urllib.request
                latest_item = None
                if pydos_vers:
                    highest_version = max(pydos_vers)
                    ver_suffix = f"{highest_version:.4f}.py" 
                    
                    for item in items:
                        if item['name'].endswith(ver_suffix):
                            latest_item = item
                            break
                    
                    if not latest_item:
                        ver_suffix_short = f"{highest_version:.2f}.py"
                        for item in items:
                            if item['name'].endswith(ver_suffix_short):
                                latest_item = item
                                break

                print("Downloading the Python file...")
                installupdate = True
                try:
                    with open(latest_item['name']) as file:
                        con = file.read
                        if con != None or len(con) >= 1:
                            installupdate = False
                except:
                    installupdate = True
                    pass
                if installupdate == True:
                    try:
                        if latest_item and 'download_url' in latest_item:
                            file_url = latest_item['download_url']
                            local_name = latest_item['name']
                            
                            import urllib.request
                            urllib.request.urlretrieve(file_url, local_name)
                            print(f"Success! Saved as {local_name}")
                        else:
                            print("Could not find the download URL for the latest version.")
                    except Exception as e:
                        print(f"Could not download file. Error: {e}")
                else:
                    print("This file already exists! To prevent overwriting, the update installation has been aborted.")
            #UPDATEMGR
            elif com == 'updatepydos':
                print("Checking for newer versions...")
                import requests
                import subprocess
                import sys
                repo_owner = "KirStudios"
                repo_name = "kirstudios"
                api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents"

                print("Contacting server...")
                response = requests.get(api_url)

                if response.status_code == 200:
                    items = response.json()
                    print("Successfully got a list of hosted versions. Comparing them to this session's version...")
                    
                    pydos_vers = []
                    for item in items:
                        filename = item['name']
                        if filename.startswith("pydos-v") and filename.endswith(".py"):
                            ver_str = filename.replace("pydos-v", "").replace(".py", "")
                            try:
                                pydos_vers.append(float(ver_str))
                            except ValueError:
                                pass
                    
                    version = float(s1)
                    print(f"All hosted versions: {pydos_vers}")
                    print(f"Current installed version: {version}")
                    if version >= max(pydos_vers):
                        if version > max(pydos_vers):
                            print("Your PY-DOS version is a build not uploaded or deleted from GitHub! Take good care of it! Your PY-DOS version is up to date!")
                            return
                        print("Your PY-DOS version is up to date! :D")
                    else:
                        print("[!] Your PY-DOS version is not up to date [!]")
                else:
                    print(f"Failed to fetch repository contents: {response.status_code}")
                    
                import urllib.request
                latest_item = None
                if pydos_vers:
                    highest_version = max(pydos_vers)
                    ver_suffix = f"{highest_version:.4f}.py" 
                    
                    for item in items:
                        if item['name'].endswith(ver_suffix):
                            latest_item = item
                            break
                    
                    if not latest_item:
                        ver_suffix_short = f"{highest_version:.2f}.py"
                        for item in items:
                            if item['name'].endswith(ver_suffix_short):
                                latest_item = item
                                break
                print("----------------------------------------\nUPDATING PY-DOS...\nDO NOT TURN OFF THIS COMPUTER OR PY-DOS DURING UPDATING\n----------------------------------------")
                print("Downloading the Python file...")
                installupdate = True
                try:
                    with open(latest_item['name']) as file:
                        con = file.read
                        if con != None or len(con) >= 1:
                            installupdate = False
                except:
                    installupdate = True
                    pass
                if installupdate == True:
                    try:
                        if latest_item and 'download_url' in latest_item:
                            file_url = latest_item['download_url']
                            local_name = latest_item['name']
                            
                            import urllib.request
                            urllib.request.urlretrieve(file_url, local_name)
                            print(f"Success! Saved as {local_name}")
                            subprocess.Popen([sys.executable, f"{local_name}"])
                            raise SystemExit
                        else:
                            print("Could not find the download URL for the latest version.")
                    except Exception as e:
                        print(f"Could not download file. Error: {e}")
                else:
                    print("This file already exists! To prevent overwriting, the update installation has been aborted.")
            elif com == 'autosavetopydrive':
                def autosaveto_pydrive(fn):
                    global savepydrive
                    import threading
                    import time
                    while True:
                        time.sleep(15)
                        fn()
                autosave = threading.Thread(target=autosaveto_pydrive)
                autosave.daemon = True
                autosave.start(s1)
            elif com == 'tts':
                import pyttsx3
                print("DOING TTS!!! ROAR!")
                try:
                    engine = pyttsx3.init()
                    engine.say(s1)
                    engine.runAndWait()
                except Exception as e:
                    print(e)
                print("donw!")
            elif com == "exe":
                import time
                import random
                import os
                import subprocess
                import sys
                try:
                    exec(s1)
                except Exception as e:
                    print(e)
            elif com == 'getpydosuptime':
                return uptime
            elif com == 'shutdown':
                import time
                global keepcounting
                raise SystemExit
            #THE END OF THE IF AND ELIFS!
            else:
                print("no commmand found.")
        except Exception as e:
            create_log(f"An error has happened while PY-DOS tried to call do(). {e}")             
    def create_log(log):
        global pydos_extend_logs
        try:
            import time
            from datetime import datetime
            now = datetime.now()

            formatted_now = now.strftime("[%Y/%m/%d_%H:%M:%S:") + now.strftime("%f")[:4] + "]"
            pydos_extend_logs.append(f"{formatted_now}{log}")
        except:
            pydos_extend_logs.append(log)

    def create_extend_file():
        with open("pydos_extend_config.txt", "w") as file:
            file.write("modules_made = False")

    def tell_extend_file_true():
        with open("pydos_extend_config.txt", "w") as file:
            file.write("modules_made = True")

    def read_extend_file():
        with open("pydos_extend_config.txt", "r") as file:
            exe = file.read()
            exe = f"global modules_made\n{exe}"
            exec(exe)
    def install_modules():
        try:
            import subprocess
            print("Installing modules PY-DOS Extend requires (press CTRL+C to cancel)...")
            global tries
            tries = 0
            beta_test = False
            if beta_test == True:
                try:
                    import requests
                    import time
                    urls = ["https://google.com", "https://microsoft.com", "https://apple.com", "https://amazon.com", "https://bing.com"]
                    for url in urls:
                        start_time = time.perf_counter()
                        response = requests.head(url, timeout=5, allow_redirects=True)
                        end_time = time.perf_counter()
                        elapsed = end_time - start_time
                except:
                    pass
                print(f"This won't take long. Set back and relax. Estimated time {elapsed}")
            elif beta_test == False:
                print("This won't take long. Set back and relax. Estimated time: 10-45 seconds")
            while True:
                print(f"ATTEMPTS TO DOWNLOAD MODULES: {tries}")
                modules_to_get = ["thefuzz", "certifi", "urllib3", "requests", "cffi", "beautifulsoup4", "pyttsx3"]
                modules = 0
                for module in modules_to_get:
                    modules = modules + 1
                    subprocess.run(
                        ["pip3", "install", module],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL
                    )
                    print(f"Attempting to install '{module}' ({modules}/{len(modules_to_get)})...")

                try:
                    import thefuzz
                    import certifi
                    import urllib3
                    import requests
                    import cffi
                    from bs4 import BeautifulSoup
                    import pyttsx3
                    break
                except KeyboardInterrupt:
                    print("Module downloading has been forcefully stopped.")
                    return
                except Exception as err:
                    print(f"An error has happened. Attemtping to redownload modules again. {err}")
                    tries = tries + 1
                    if tries >= 3:
                        print("Too many failed attempts has happened. PY-DOS Extend will now exit.")
                        raise SystemExit
            tell_extend_file_true()
        except:
            return
    try:
        if debug:
            print("Reading PY-DOS Extend config file...")
        read_extend_file()
        modules_made = True
    except Exception as e:
        create_log(f"An error has happened while trying to read config file. {e}")
        try:
            create_extend_file()
        except Exception as e:
            create_log(f"An error has happened while trying to write config file. {e}")
            print(f"Unable to create PY-DOS Extend Configuration File. {e}")
    if modules_made == False:
        install_modules()
    else:
        try:
            import thefuzz
            import certifi
            import urllib3
            import requests
            import cffi
            from bs4 import BeautifulSoup
            import pyttsx3
        except ModuleNotFoundError:
            install_modules()

except Exception as err:
    print(f"A problem with PY-DOS Extend happened. Error: {err}")