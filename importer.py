import sys 
from importlib import import_module

def dynamic_import(Name):
    terminal = sys.argv 

    if len(terminal) == 1 or terminal[1] == "help":
        Name = "help"
        return import_module(Name)


    elif terminal[1] == "volunteer":
        Name = "volunteer"
        return import_module(Name)


    elif terminal[1] == "book":
        Name = "booking_system"
        return import_module(Name)


    elif terminal[1] == "cancel_volunteer":
        Name = "cancel_volunteer"
        return import_module(Name)


    elif terminal[1] == "cancel_booking":
        Name = "cancel_booking"
        return import_module(Name)
        

    