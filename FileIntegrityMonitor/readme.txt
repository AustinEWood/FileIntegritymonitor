This is a simple file integrity monitor written in python named File Casket.

I will be working on this regularly until it is done.

For now, it is remarkably simple.

Put it in the main directory of the files you would like to monitor.

Run filecasket.py in console.

Make the selection you would like select Hash, Check, or Clear.

Hash:
File name and type will be needed as so readme.txt this will find the file in the directory hash it and save it to the log file. As long as there is only one file with that name. I am working on how to handle files with the same name.

Check:
will find the file in the directory hash it and check the log file to see if the hash has changed. If the has has not changed it will tel you found in file, if the hash has changed it will say not found. As long as there is only one file with that name. I am working on how to handle files with the same name.

Clear:
will do just that clear the log file.

For now the log file will save the location and name of the file on the first line, the hash on the second line, and the time and date of the hash will save under that.

I have many more features coming, please let me know of any ideas or anything I can fix!!!

future features:
constant running and check of file already hashed.
alert if file has changed.
hash all files in directory at one time.


this is a test