#!/usr/bin/env python
import hashlib
import os


print('Thank you for using File Casket...')

directory = "/home/kali/Documents/projects/FileIntegrityMonitor/"

FileName = directory + input("File Name: ")

with open(FileName, "rb") as f:
    file_hash = hashlib.md5()
    while chunk := f.read(8192):
        file_hash.update(chunk)
        (file_hash.digest())

print(file_hash.hexdigest())  
