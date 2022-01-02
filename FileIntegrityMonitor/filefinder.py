#!/usr/bin/env python
from pathlib import Path
import os


# get path to current working directory
# ask for file name will walk all directorys inside the one you are in
# will find all files with that name and return path

try:
    def get_file():
        name = input("File name:")
        path = Path.cwd()
        for root, dirs, files in os.walk(path):
            if name in files:
                path_to_file = (os.path.join(root, name))
                return path_to_file
                return name
except:
    print("Error 1")
