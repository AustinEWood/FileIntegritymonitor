from hashfile import hash_file
from clear import clear_file
from check_hash import recheck


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
        print("That is not a choice....")
        print("Enter hash or check or clear no spaces no upper case")
        print("Goodbye!")
except:
    print("No file with that name...")
    print("Check the spelling")
    print("File type must be added as so readme.txt")
    print("Goodbye!")
