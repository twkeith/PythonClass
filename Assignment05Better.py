# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# KBurdette,2.18.2020, added assignment parts
# ------------------------------------------------------------------------ #

import os

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python Dictionary.
# TODO: Add Code Here
if os.path.exists(objFile):
    ReaderFileObj = open(objFile, "r")

    for row in ReaderFileObj:
        TaskPair = row.split(",")
        lstTable.append({"task" : TaskPair[0], "priority" : TaskPair[1].strip()})

    ReaderFileObj.close()
else:
    print("Somehow you have nothing to do")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new l1ine for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        if len(lstTable) == 0:
            print("Somehow you have nothing to do")
        for row in lstTable:
            print(f'{row["task"]} - {row["priority"]}')
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        TextTask = input("What task do you need to accomplish: ")
        TextPriority = input("What is this task's priority: ")
        lstTable.append({"task" : TextTask, "priority" : TextPriority})
        continue
    # Step 5 - Remove a new item to the list/Table
    elif (strChoice.strip() == '3'):
        TaskDone = input("Which task did you complete: ")
        FindFlag = False
        i = 0
        popList = []
        for row in lstTable:
            if TaskDone == row['task']:
                FindFlag = True
                popList.append(i)
            i += 1

        if not FindFlag:
            print(f"{TaskDone} was not on your ToDo list.")
        else:
            howmanypopped = 0
            for j in popList:
                print(f"{lstTable[j - howmanypopped]} will be removed")
                lstTable.pop(j - howmanypopped)
                howmanypopped += 1
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        WriteFileObj = open(objFile, "w")
        for row in lstTable:
            WriteFileObj.write(row["task"] + ',' + row["priority"] + '\n')
        WriteFileObj.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        print("If you did not save, your ToDo list will not be updated")
        break  # and Exit the program
