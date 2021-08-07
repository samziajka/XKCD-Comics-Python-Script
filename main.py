"""
XKCD Scripting Tasks
"""

# Import modules
import os

# Inform the user what the options are
print("""Thank you for choosing to run this script, please select from the following options:
    
Enter 1 to download the most recent 7 editions of XKCD comics
and store them as a zip file with a summary of their metadata.

Enter 2 to read the zip file and print which editions are stored
and how many editions were published on each date.\n""")

# Enter an input
user_input = input("Select which task you would like to run: ")

# Run a script dependent on the user input
if user_input == "1":
    print("\nRunning Script 1\n")
    os.system("python task_1.py 1")
elif user_input == "2":
    print("\nRunning Script 2\n")
    os.system("python task_2.py 1")
else:
    print("\nPlease run this script again and enter either 1 or 2.")