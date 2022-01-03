import os
import hashlib
import logging
import datetime
from pathlib import Path


# Get date and time from the current os
datetime_class = datetime.datetime.now()
# Get file to log information to
logging.basicConfig(filename="logfile.log", level=logging.DEBUG)

try:
    def error_handle(errorcode):
        if(errorcode == 1):
            print("Invalid File")
            if(errorcode == 2):
                print("Did not work")
except:
    print("Critical error")

# clear file function
try:
    def clear_file():  # Define function
        # Open log file in write mode this will erase it
        log_clear = open("logfile.log", "w")
        log_clear.close()  # close log file
        print("File has been cleared")
except:
    error_handle(2)  # if error message

# Get file function
try:
    def get_file():  # Define function
        name = input("File name:")  # Get file name
        path = Path.cwd()  # Get current working directory name it path
        # Walk from current working directory to were the file is
        for root, dirs, files in os.walk(path):
            if name in files:  # Check for file name in directory
                # Get whole path of the file
                path_to_file = (os.path.join(root, name))
                return path_to_file
except:
    error_handle(2)

# Hash file and save to file
try:
    def hash_file():
        path_to_file = get_file()
        with open(path_to_file, "rb") as f:
            file_hash = hashlib.md5()
            while chunk := f.read(8192):
                file_hash.update(chunk)
                (file_hash.digest())
                print(file_hash.hexdigest())
                logging.info(path_to_file)
                logging.info(file_hash.hexdigest())
                logging.info(datetime_class)
except:
    error_handle(2)

try:
    def recheck():
        path_to_file = get_file()

        with open(path_to_file, "rb") as f:
            file_hash = hashlib.md5()
            while chunk := f.read(8192):
                file_hash.update(chunk)
                (file_hash.digest())
                print(file_hash.hexdigest())
                check__hash = file_hash.hexdigest()

        log_check = open("logfile.log", "r")
        read_log = log_check.read()
        if check__hash in read_log:
            print("hash", file_hash.hexdigest(), "found in file")
        else:
            print("hash", file_hash.hexdigest(), "not found")
except:
    error_handle(2)


print("hash or check or clear")
choice = input("")

try:
    if choice == "hash":
        hash_file()
    elif choice == "clear":
        clear_file()
    elif choice == "check":
        recheck()
    else:
        error_handle(1)
except:
    error_handle(1)
