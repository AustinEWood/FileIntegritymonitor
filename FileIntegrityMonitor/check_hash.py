from filefinder import get_file
import logging
import datetime
import hashlib


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

                log_check.close()
