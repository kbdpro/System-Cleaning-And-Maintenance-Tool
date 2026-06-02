import os
import shutil
import psutil

temp_folder = os.environ.get('TEMP')
BLACK_LIST = ["chrome.exe", "discord.exe", "spotify.exe", "zenbrowser.exe", "brave.exe"] #If there are any important apps that you use frequently, you can add them here; however, we do not recommend adding apps that you do not use very often

def temp_clear():
    print("The system is being cleaned up. None of your data will be deleted...")
    
    for file_name in os.listdir(temp_folder):
        file_patch = os.path.join(temp_folder, file_name)
        try:
            if os.path.isfile(file_patch) or os.path.islink(file_patch):
                os.unlink(file_patch)
            elif os.path.isdir(file_patch):
                shutil.rmtree(file_patch)
        except Exception as e:
            continue

def clear_processes():
    print("Scanning background processes...")
    
    for operation in psutil.process_iter(['name']):
        try:
            operation_name = operation.info['name']
            
            if operation_name in BLACK_LIST:
                operation.terminate()
                print(f"-> {operation_name} is closed and RAM Cleared")
                
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

if __name__ == "__main__":
    temp_clear()
    clear_processes()
    print("Cleaning Completed")