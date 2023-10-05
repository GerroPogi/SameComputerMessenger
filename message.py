import os
import datetime
if not os.path.exists(os.path.join(os.path.dirname(__file__),"files")):
    os.mkdir(os.path.join(os.path.dirname(__file__),"files"))
elif not os.path.exists(os.path.join(os.path.dirname(__file__),"files","messages.txt")):
    with open(os.path.join(os.path.dirname(__file__),"files","messages.txt"),'w') as f:
        f.write("Messages:")
Fmessages=os.path.join(os.path.dirname(__file__),"files","messages.txt")
dt=datetime.datetime.now()


while True:
    print(f"Hi welcome to Computer 33!!\nThis is for other people to message other people in this computer.\nYou can message other people using this computer like mails.\nPlease be nice to other people, and please tell the chat if you want more improvements.\n")
    with open(Fmessages, "r") as f:
        print(f.read())
    message=input()
    if len(message)==0:
        pass
    else:
        with open(Fmessages, "a") as f:
            f.write(f"\n{dt.strftime('%Y-%m-%d: %I:%M %p')}: {message}")
    os.system("cls")