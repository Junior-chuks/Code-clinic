#!/usr/bin/python3

import sys
import quickstart
import os.path
from importer import dynamic_import

# selects the desired file to import based off the commands passed in by the user
file = dynamic_import(None)


# stores the argument passed in from the terminal by the user in a list
terminal = sys.argv 


def commands():
    """
    Executes certain functions from their allocated files according to the argument found in the terminal
    """
    if len(terminal)== 1 or terminal[1] == "help" :
        file.helper()


    elif terminal[1] == "view_calendar":
        quickstart.view_calendar(1)


    elif terminal[1] == "login":
        quickstart.login()


    elif terminal[1] == "logout":
        quickstart.logout()


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
        

if __name__ == "__main__":
    commands()
