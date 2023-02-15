import sys
import quickstart
import os.path
import volunteer

terminal = sys.argv 

if terminal[1] == "view_calendar":
    quickstart.view_calendar(1)

if terminal[1] == "login":
    if os.path.exists('tokens.json') :
        print("Already logged in")
    
    else:
        quickstart.file_update(1)
        print("Login successful")


if terminal[1] == "volunteer":
    volunteer.slot_checker()
    quickstart.file_update(1)

# if terminal[1] == "Volunteer":




