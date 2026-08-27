try:
    print("Hi! Welcome to PY-DOS Extend!")
    pydos_extend_logs = []
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

    def read_extend_file():
        with open("pydos_extend_config.txt", "r") as file:
            exe = file.read()
            exec(exe)

    try:
        read_extend_file()
    except Exception as e:
        create_log(f"An error has happened while trying to read config file. {e}")
        try:
            create_extend_file()
        except Exception as e:
            create_log(f"An error has happened while trying to read config file. {e}")
            print("Unable to create PY-DOS Extend Configuration File. View details in logs.")
            print(pydos_extend_logs)
            input()
except Exception as err:
    print(f"A problem with PY-DOS Extend happened. Error: {err}")