import os
import shutil

temp_folder = os.environ.get('TEMP')

def temp_clear():
    print("The system is being cleaned up. None of your data will be deleted...")

for file_name in os.listdir(temp_folder):
        file_patch = os.path.join(temp_folder, file_name)
        try:
            if os.path.isfile(file_patch) or os.path.islink(file_patch):
                os.unlink(file_patch)
            elif os.path.isdir():
                shutil.rmtree(file_patch)
        except Exception as e:
            continue

if __name__ == "__main__":
    temp_clear()
    print("Cleaning Completed")