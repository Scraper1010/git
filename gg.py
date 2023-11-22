import subprocess
import os

def git():
    def clear():
        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')

    current_script_path = os.path.abspath(__file__)
    current_folder_path = os.path.dirname(current_script_path)

    print(current_folder_path)

    # Check if the repository is already initialized
    is_repo_initialized = os.path.exists(os.path.join(current_folder_path, '.git'))

    if not is_repo_initialized:
        # If not initialized, initialize the repository and add the remote origin
        commands = f'cd {current_folder_path} && git init && git remote add origin https://github.com/Scraper1010/git.git && git pull origin master'

        try:
            # Run the combined shell commands
            subprocess.check_call(commands, shell=True)
            print("Command executed successfully")
        except subprocess.CalledProcessError as e:
            print(f"Error during command execution: {e}")
    else:
        # If repository is already initialized, run git pull
        pull_command = f'cd {current_folder_path} && git pull origin master'
        try:
            subprocess.check_call(pull_command, shell=True)
            print("Git pull executed successfully")
        except subprocess.CalledProcessError as e:
            print(f"Error during git pull execution: {e}")

