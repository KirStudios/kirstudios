try:
    dev = "Kir Studios"
    mainapp = "PY-DOS"
    #BOTH PY-DOS AND PY-DOS EXTEND ARE MADE BY KIR STUDIOS
    if __name__ != "__main__":
        input("Hi! Welcome to PY-DOS Extend! So glad you have installed this PY-DOS Application, but this PY-DOS Application requires you to run it in PY-DOS. Press ENTER to exit.")
        raise SystemExit
    global modules_made, pydos_extend_logs
    modules_made = False
    pydos_extend_logs = []
    def do(com):
         if com == 'unknowncom':
            from thefuzz import process

            # Extract the single best match
            result = process.extractOne(command, commands)

            # Check if a match was found and if its score is 85 or higher
            if result and result[1] >= 85:
                best_match = result[0]
            else:
                best_match = None

            print(best_match)

         pass
    def create_log(log):
        global pydos_extend_logs
        try:
            import time
            from datetime import datetime
            now = datetime.now()

            # %f gives 6 digits of microseconds; slice to keep the first 4 digits
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
            print("Unable to create PY-DOS Extend Configuration File. View details in logs.")
    if modules_made == False:
        import subprocess
        print("Installing modules PY-DOS Extend requires...")
        global tries
        tries = 0
        while True:
            print(f"ATTEMPTS TO DOWNLOAD MODULES: {tries}")
            modules_to_get = ["thefuzz", "certifi", "urllib3", "requests", "cffi", "numpy"]
            for module in modules_to_get:
                subprocess.run(["pip", "install", f"{module}"])
            try:
                import thefuzz
                import certifi
                import urllib3
                import requests
                import cffi
                import numpy
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