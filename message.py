import os
import datetime
"""
    Author: GerroPogi
    Version: 0.1
    Name: SameComputerMessenger
    Link: https://github.com/GerroPogi/SameComputerMessenger
"""

# Checks for "file" folder and "message.txt" in the file directory of the file.
if not os.path.exists(os.path.join(os.path.dirname(__file__),"files")):
    os.mkdir(os.path.join(os.path.dirname(__file__),"files"))
elif not os.path.exists(os.path.join(os.path.dirname(__file__),"files","messages.txt")):
    with open(os.path.join(os.path.dirname(__file__),"files","messages.txt"),'w') as f:
        f.write("Messages:")
# Makes file location of the message file
Fmessages=os.path.join(os.path.dirname(__file__),"files","messages.txt")


# Initialization
while True:
    # Makes the variable of the time now to show to messages.
    dt=datetime.datetime.now()
    print(f"Hi welcome to Computer 33!!\nThis is for other people to message other people in this computer.\nYou can message other people using this computer like mails.\nPlease be nice to other people, and please tell the chat if you want more improvements.\n")
    # Prints the message log
    with open(Fmessages, "r") as f:
        print(f.read())
    # Gets message data
    message=input()
    #Checks if the message is empty or not
    if len(message)==0:
        pass
    else:
         # If not empty then it can append to the message log with the date and time with the message.
        with open(Fmessages, "a") as f:
            f.write(f"\n{dt.strftime('%Y-%m-%d: %I:%M %p')}: {message}")
    #So that the print statements won't overlap
    os.system("cls")
