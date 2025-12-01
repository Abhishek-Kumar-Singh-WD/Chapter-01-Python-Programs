# This program prints the list of files and folders at the path entered by the user.

import os

path = input("Enter the path : ")

try:
    print("The list of files and folders at the path is : ")

    contents = os.listdir(path)
    
    for item in contents:
        print(item)

except FileNotFoundError:
    print("The path is not found.")
except PermissionError:
    print("The path is not access.")
