#!/usr/bin/python3

import sys
import quickstart
import os.path
import click #proffesional CLI(command line interface) 
from importer import dynamic_import

# selects the desired file to import based off the commands passed in by the user
file = dynamic_import(None)


# stores the argument passed in from the terminal by the user in a list
# terminal = sys.argv 

@click.command()
@click.argument("terminal",default = "")
def commands(terminal):
    """
    Executes certain functions from their allocated files according to the argument found in the terminal
    """
    if len(terminal) == 0 or terminal == "help" :
        file.helper()
#   if len(terminal[1]) == 0 or terminal[1] == help:
#       file.helper()
    elif terminal == "view_calendar":
        quickstart.view_calendar(1)


    elif terminal == "login":
        quickstart.login()


    elif terminal == "logout":
        quickstart.logout()


    elif terminal == "volunteer":
        file.slot_checker()
        quickstart.file_update(1)


    elif terminal == "book":
        file.booking_engine()
        quickstart.file_update(1)


    elif terminal == "cancel_volunteer":
        num = file.cancel_engine()

        if num > 0:
            quickstart.file_update(1)


    elif terminal == "cancel_booking":
        num = file.cancel_engine()

        if num > 0 :
            quickstart.file_update(1)
        

if __name__ == "__main__":
    sys.exit(commands())
