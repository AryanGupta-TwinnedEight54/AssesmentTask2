# Made by Caden
# Imports 'subprocess' and 'os' libraries.
import subprocess
import os
# Sets variable 'dir_path' to the directory name of where the file is located.
dir_path = os.path.dirname(os.path.abspath(__file__))
# Sets 'check' variable to '1' to allow the program to begin running.
check = 1
# Print statements for debugging.
#print (dir_path)
#print (__file__)
# Provides the user an explanation for what the two programs within the program do and provides a choice of what program they wish to run.
print("Welcome to the Tram Timetable Program!")
print("")
print("If you would like to see a linear example of trams running in a system with dynamic passenger boarding amounts, enter '1'.")
print("")
print("If you would like to see an example of a timetable of trams running in a system from 6:30am - 7:00pm, enter '2'.")
print("")
# Begins program loop if 'check' is set to '1'.
while check == 1:
    # Asks the user to input which program they want to run.
    choice = input("Please enter '1' or '2' here. ")
    # If the user inputted '1', the program runs the linear output and then ends the while loop.
    if choice == "1":
        subprocess.run(["python", dir_path + "\\Code1.py"])
        check = 0
    # If the user inputted '2', the program runs the timetable output and then ends the while loop.
    elif choice == "2":
        subprocess.run(["python", dir_path + "\\timetable.py"])
        check = 0
    # If the user made an input that was not an available option of either '1' or '2', it will print that it is invalid and ask them to restate their input, starting the loop again.
    else:
        print("")
        print ("Invalid input. Please try again.")
        print("")
        

