import os
import hashlib
import logging
import datetime
from pathlib import Path


# Get date and time from the current os define it in a variable
datetime_class = datetime.datetime.now()
# Declare file to log information to
logging.basicConfig(filename="logfile.log", level=logging.DEBUG)

try:
    def error_handle(errorcode):  # Define function
        if(errorcode == 1):
            print("Invalid File")
        elif(errorcode == 2):
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
    error_handle(2)  # Error message

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

# Hash file and log to file function
try:
    def hash_file():  # Define function
        path_to_file = get_file()  # Run get_file function to get path
        with open(path_to_file, "rb") as f:  # Open path to find file
            file_hash = hashlib.md5()  # Hash file
            while chunk := f.read(8192):
                file_hash.update(chunk)
                (file_hash.digest())
                print(file_hash.hexdigest())  # Print Hash
                logging.info(path_to_file)  # Log path and name of file
                logging.info(file_hash.hexdigest())  # Log hash
                # Log date and time file was hashed
                logging.info(datetime_class)
except:
    error_handle(2)  # Error message

# check log file for hash a hash function
try:
    def recheck():  # Define function
        path_to_file = get_file()  # Run get_file function to get path

        with open(path_to_file, "rb") as f:  # Open path to find file
            file_hash = hashlib.md5()   # Hash file
            while chunk := f.read(8192):
                file_hash.update(chunk)
                (file_hash.digest())
                print(file_hash.hexdigest())  # Print hash
                check__hash = file_hash.hexdigest()  # Save hash to variable

        log_check = open("logfile.log", "r")  # Save log file to variable
        read_log = log_check.read()  # Save read log file to variable
        if check__hash in read_log:  # Check log file for hash
            print("hash", file_hash.hexdigest(),
                  "found in file")  # If hash found print
        else:
            # If hash not found print
            print("hash", file_hash.hexdigest(), "not found")
except:
    error_handle(2)  # Error message


# Ask what function to do
def main():  # Define function
    try:
        if choice == "hash":  # If choice hash run hash_file function
            hash_file()
        elif choice == "clear":  # If choice clear run clear_file function
            clear_file()
        elif choice == "check":  # If choice check run recheck function
            recheck()
        else:
            error_handle(1)  # Error message
    except:
        error_handle(1)  # Error message


# While loop to keep the programe running until you want to end it
while True:
    print("hash or check or clear or exit")  # Print message
    choice = input("")  # Ask for input
    if choice == "exit":  # Stop loop if input exit
        break
    else:
        main()  # Run main function if input anythin but exit
        if input("Would you like to do more y/n:") == 'n':  # Ask for input
            break  # Break loop if input n
