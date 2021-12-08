#!/usr/bin/env python
import hashlib
import os
import time
import schedule
import logging

logging.basicConfig(filename='logfile.log', level=logging.DEBUG)

print('Thank you for using File Casket...')

time.sleep(1)

print("What would you like to do?")

time.sleep(1)

print("hash file, clear log, exit")

choice = str(input())

exit = "exit"

hash = "hash file"

clear = "clear log"

directory = "/home/kali/Documents/projects/FileIntegrityMonitor/"

if choice == hash:
    FileName = input("File Name:")

    Location = directory + FileName

    try:
        with open(Location, "rb") as f:
            file_hash = hashlib.md5()
            while chunk := f.read(8192):
                file_hash.update(chunk)
                (file_hash.digest())

        logging.info(FileName)  # this is how I log the hash to log file
        logging.info(file_hash.hexdigest())

        print(file_hash.hexdigest())
    except:
        print("File not found!")
        print("Please try again...")
elif choice == exit:
    print("Thank you come again...")

elif choice == clear:
    a_file = open('logfile.log', 'w')  # this is how I clear the log file
    a_file.truncate()
    a_file.close()
