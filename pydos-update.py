if __name__ != "main":
    def pydosupdate():
        if exever == True:
            import requests
            print("Checking for newer versions...")

            # GitHub API URL for the repository's contents (defaults to the root directory)
            repo_owner = "KirStudios"
            repo_name = "kirstudios"
            api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents"

            print("Contacting server...")
            response = requests.get(api_url)

            if response.status_code == 200:
                items = response.json()
                print("Successfully got a list of hosted versions. Comparing them to this sessions version...")
                pydos_vers = []
                for item in items:
                    # Check whether it's a file or directory
                    item_type = item["type"]  # "file" or "dir"
                    git_filename = item['name'][7:]
                    if ".py" in git_filename:
                        temp = git_filename.replace(".py", "")
                        pydos_vers.append(float(temp))

                print(f"All hosted versions: {pydos_vers}")
                print(f"Current installed version: {version}")
                if version >= max(pydos_vers):
                    print("Your PY-DOS version is up to date!")
                else:
                    print("Your PY-DOS version is not up to date [!]")

                    
            else:
                print(f"Failed to fetch repository contents: {response.status_code}")
        else:
            print("This function cannot be ran because your edition of PY-DOS do not support it. PY-DOS Update")
else:
    print("This PY-DOS Application requires you to run it in PY-DOS.")
    input("Press ENTER to exit this PY-DOS Application.")