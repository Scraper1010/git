def git():
    import subprocess
    import os

    def clear():
            if os.name == 'nt':
                _ = os.system('cls')
            else:
                _ = os.system('clear')
            if os.name == 'nt':
                slash= "\\"
            else:
                slash= "/"

    current_script_path = os.path.abspath(__file__)
    current_folder_path = os.path.dirname(current_script_path)

    print(current_folder_path)

    commands = f'cd {current_folder_path} && git init && git remote add origin https://github.com/Scraper1010/git.git && git pull origin master'

    try:
        # Run the combined shell commands
        subprocess.check_call(commands, shell=True)
        print("Command executed successfully")
    except subprocess.CalledProcessError as e:
        print(f"Error during command execution: {e}")