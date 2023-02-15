#!/usr/bin/python3

import sys
import quickstart
import os.path
from importer import dynamic_import

file = dynamic_import(None)

terminal = sys.argv 

if len(terminal)== 1 or terminal[1] == "help" :
    file.helper()


elif terminal[1] == "view_calendar":
    quickstart.view_calendar(1)


elif terminal[1] == "login":
    if os.path.exists('tokens.json') :
        print("Already logged in")
    
    else:
        quickstart.file_update(1)
        print("Login successful")


elif terminal[1] == "volunteer":
    file.slot_checker()
    quickstart.file_update(1)


elif terminal[1] == "book":
    file.booking_engine()
    quickstart.file_update(1)


elif terminal[1] == "cancel_volunteer":
    num = file.cancel_engine()

    if num > 0:
        quickstart.file_update(1)


elif terminal[1] == "cancel_booking":
    num = file.cancel_engine()

    if num > 0 :
        quickstart.file_update(1)
    
