#!/usr/bin/env python
def clear_file():
    log_clear = open("logfile.log", "w")
    log_clear.close()
    print("File has been cleared")
