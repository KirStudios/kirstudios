try:
    dev = "Kir Studios"
    mainapp = "PY-DOS"
    #BOTH PY-DOS AND PY-DOS EXTEND ARE MADE BY KIR STUDIOS
    if __name__ == "__main__":
        input("Hi! Welcome to PY-DOS Extend! So glad you have installed this PY-DOS Application, but this PY-DOS Application requires you to run it in PY-DOS. Press ENTER to exit.")
        raise SystemExit
    global modules_made, pydos_extend_logs, savepydrive
    modules_made = False
    import threading
    pydos_extend_logs = []
    #WHAT PY-DOS CALLS TO DO
    def do(com=None, s1=None, s2=None, s3=None, s4=None, s5=None):
        try:
            global pydocommand, commands
            #USER TYPES UNKNOWN COMMAND
            if com == 'unknowncom':
                from thefuzz import process

                result = process.extractOne(s1, s2)

                if result and result[1] >= 80:
                    best_match = result[0]
                else:
                    best_match = None

                output = f"Perhaps you meant to type '{best_match}'?"
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
                            print("Your PY-DOS version is up to date!")
                        else:
                            print("Your PY-DOS version is not up to date [!]")
                    else:
                        print("No valid version files found on server.")
                else:
                    print(f"Failed to fetch repository contents: {response.status_code}")
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
            elif com == 'autosavetopydrive':
                def autosaveto_pydrive(fn):
                    global savepydrive
                    import threading
                    import time
                    while True:
                        time.sleep(15)
                        fn()
                my_thread = threading.Thread(target=autosaveto_pydrive)
                my_thread.start(s1)
            #THE END OF THE IF AND ELIFS!
            elif com == 'tts':
                import pyttsx3
                print("DOING TTS!!! ROAR!")
                try:
                    engine = pyttsx3.init()

                    # 2. Queue the text you want to speak
                    engine.say(s1)
                    engine.runAndWait()
                except Exception as e:
                    print(e)
                print("donw!")
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

    try:
        read_extend_file()
    except Exception as e:
        create_log(f"An error has happened while trying to read config file. {e}")
        try:
            create_extend_file()
        except Exception as e:
            create_log(f"An error has happened while trying to write config file. {e}")
            print(f"Unable to create PY-DOS Extend Configuration File. {e}")
    if modules_made == False:
        import subprocess
        print("Installing modules PY-DOS Extend requires...")
        global tries
        tries = 0
        while True:
            print(f"ATTEMPTS TO DOWNLOAD MODULES: {tries}")
            modules_to_get = ["thefuzz", "certifi", "urllib3", "requests", "cffi", "beautifulsoup4", "pyttsx3"]
            for module in modules_to_get:
                subprocess.run(["pip3", "install", f"{module}"])
            try:
                import thefuzz
                import certifi
                import urllib3
                import requests
                import cffi
                from bs4 import BeautifulSoup
                import pyttsx3
                break
            except Exception as err:
                print(f"An error has happened. Attemtping to redownload modules again. {err}")
                tries = tries + 1
                if tries >= 3:
                    print("Too many failed attempts has happened. PY-DOS Extend will now exit.")
                    raise SystemExit
        tell_extend_file_true()
        

except Exception as err:
    print(f"A problem with PY-DOS Extend happened. Error: {err}")