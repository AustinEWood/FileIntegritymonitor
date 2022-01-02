#!/usr/bin/env python
import hashlib
from filefinder import get_file
import logging
import datetime

# Get date and time from the current os
datetime_class = datetime.datetime.now()
# Get file to log information to
logging.basicConfig(filename="logfile.log", level=logging.DEBUG)


#Hash file and save to file
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
    print("Error 2")
