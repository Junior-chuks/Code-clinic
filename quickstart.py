from __future__ import print_function

import datetime
import os.path
import os as so
import sys
from tabulate import tabulate

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

# returns code clinic calendar credentials
def main_clinic():
    """
    Retrieves calendar credentials through authorization flow
        after the user has signed in
    return: creds
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        print("Please click the link below to sign into Code Clinic calendar\n"
                "Use the following login details:\n"
                "Email: codeclinic123@gmail.com\n"
                "Password: codeclinc_1")
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    current_date = str(datetime.date.today())
    print(current_date)
    message = "\nCode Clinic Calendar 7 days view\n"
    calendar(creds,message)
    return creds

# returns student credentials
def main_student():
    """
    Retrieves calendar credentials through authorization flow
        after the user has signed in
    return: creds
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('tokens.json'):
        creds = Credentials.from_authorized_user_file('tokens.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        print("Please click the link below to sign into your Student calendar\n")
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('tokens.json', 'w') as token:
            token.write(creds.to_json())

    message = "Student Calendar 7 days view\n"
    calendar(creds,message)
    

def calendar(creds,mesg):
    """
    Displays a title for the calendar data based on the string passed in as the parameter for mesg
    Displays both upcoming and no upcoming event according to credentails passed in as a parameter
    Param: creds, mesg
    """
    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print(mesg)
        print('Getting the upcoming 7 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=7, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])


        # Prints the date ,time and task of the next 7 days of calendar data
        if not events:
            no_upcoming_event(events)
        else:
            upcoming_event(events)
        
    except HttpError as error:
        print('An error occurred: %s' % error)
        

def upcoming_event(events):
    """
    Iterates through a list valid events from the calendar to decided suitable formats to display the data
    Param: events
    """
        
    dai = 0

    current_time = str(datetime.datetime.now().strftime("%H:%M"))
    current_date  = str(datetime.date.today())
    lis_date = current_date.split("-")
    dai += int(lis_date[-1])
    days = 7
    lis_day = []
    month,lenght,lis_day = end_month_monitor(dai,lis_day,lis_date)

    indexes = 0
    indexe = 0
    lis_events = []
    day_2 = []
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        date_time = start.split("T")
        
        if len(date_time) == 2:
            events_set = [date_time[0],date_time[1], event['summary']]
            
        else:
            events_set = " - ".join([date_time[0]," ** ** ** ", event['summary']])
        day = date_time[0].split("-")
        day_1 = int(day[-1])
        lis_events.append(events_set)
        day_2.append(day_1)

    lis_data = []
    while True:
        if lenght >0 :
            next_day = [day[0],day[1],str(lis_day[indexes])]
        else:
            next_day = [day[0],str(month),str(lis_day[indexes])]
        
        # if days == 7 :
        #     print("Date \t \ttime \t\ttask\n")
        
        if  lis_day[indexes] == day_2[indexe] :
            
            n = indexe 
            t = 0

            for i in day_2 :
                if i == lis_day[indexes]:
                    # print(lis_events[n],"\n")
                    lis_data.append(lis_events[n])
                    t+=1
                    n+=1 
            if len(day_2) > 1 or t>0 :
                indexe+=t
                if len(day_2) == indexe:
                    indexe -=1
            
        else:
            # print(" - ".join(next_day),"no event\n")
            lis_data.append([" - ".join(next_day),current_time,"no event\n"])

        indexes+=1
        days -=1
        lenght-=1
        if days == 0:
            break
    print(tabulate(lis_data,["Date","Time ","Task"],"double_outline"))


def no_upcoming_event(events):
        """
        Iterates through an empyt list of data from the calendar to display a default format
        Param: events
        """
        
        dai = 0
        
        current_date  = str(datetime.date.today())
        current_time = str(datetime.datetime.now().strftime("%H:%M"))
        lis_date = current_date.split("-")
        
        dai += int(lis_date[-1])
        lis_day = []

        days = 7
        indexes = 0
        month,lenght,lis_day = end_month_monitor(dai,lis_day,lis_date)

        if not events:
            day = lis_date[:3]

        lis_data = []
        while True:
            
            if lenght >0 :
                next_day = [day[0],day[1],str(lis_day[indexes])]
            else:
                next_day = [day[0],str(month),str(lis_day[indexes])]
            
            # if days == 7 :
            #     print("Date \t \ttime \t\ttask\n")
            #     lis_date.append(["Date","time ","task"])
            
            # print(" - ".join(next_day)+" no event\n")
            lis_data.append([" - ".join(next_day),current_time," no event"])
            
            indexes+=1
            days -=1
            lenght -= 1
            if days == 0:
                break
        print(tabulate(lis_data,["Date","Time ","Task"],"double_outline"))
    

def end_month_monitor(dai,lis_day,lis_date):
    """
    Tracks the end of the month to increment properly into the next month
    Param: dai, lis_day, lis_date
    return: month, lenght, lis_day
    """
    lenght =0
    month = int(lis_date[1]) + 1
    months = ["01", "03", "05", "07", "08", "10", "12"]
    monthz = ["04","06","09","11"]
    month_leap = ["02"]
    for i in range(7):
        
        if dai <= 31 and lis_date[1] in months :
            lis_day.append(dai)
            dai+=1

        if dai <= 30 and lis_date[1] in monthz :
            lis_day.append(dai)
            dai+=1

        if dai <= 28 and lis_date[1] in month_leap :
            lis_day.append(dai)
            dai+=1
        lenght = len(lis_day)

    l = 0
    if len(lis_day) < 7 :
        dai = 0
        c = len(lis_day) 
        lenght = c
        l+=1
        n = 7 - c 

        for i in range(n):
            if dai <= 31 and lis_date[1] in months :
                dai+=1
                lis_day.append(dai)
            
            if dai <= 30 and lis_date[1] in monthz :
                dai+=1
                lis_day.append(dai)
    return month,lenght,lis_day
   
        
def view_calendar(count):
    """
    Displays the two calendar 7 days of event data
    Param: count
    """
    main_clinic()
    main_student()

    today = str(datetime.date.today())

    if os.path.exists('calendar.txt') :
        with open("calendar.txt","r") as file :
            date = file.readline().strip("\n")
       
    
    if not os.path.exists('calendar.txt'):
        file_update(count)
       
    
    elif date != today  :
        file_update(count)


def file_update(num):
    """
    Downloads a file that stores both calendar data worth 7 days
    and continues to update the existing file whenever it's called upon
    Param: num
    """
    if os.path.exists("calendar.txt"):

        mess = "\nUpdating file:"
        mess_2 = "\nFile update complete."

    else:
        mess = "\nDownloading file:"
        mess_2 = "\nFile download complete."

    original_stdout = sys.stdout
    if num == 0:
       return  
    with open("calendar.txt","w") as sys.stdout:
        num-=1
        view_calendar(num)
        sys.stdout = original_stdout
    loader_animation(mess,mess_2)


def login():
    """
    Prompts the user to login to both calendar
    """
    if os.path.exists('tokens.json') :
        print("Already logged in")
    
    else:
        blockPrint()
        file_update(1)
        enablePrint()
        print("Login successful. :)")


def blockPrint():
    """
    Blocks out any print statements from being displayed
    """
    sys.stdout = open(so.devnull, 'w')


def enablePrint():
    """
    Allows print statements to be displayed
    """
    sys.stdout = sys.__stdout__


def logout():
    """
    Prompts the user to logout of both calendar
    """
    if os.path.exists("tokens.json"):
        so.remove("tokens.json")
        so.remove("token.json")
        print("Logout successful. :)")
    else:
        print("Already logged out.")


def loader_animation(message,message_2):
    """
    Creates a loading animation that's displayed on the user interface
    Param: message,message_2
    """
    import time
    import sys
    print(message)

    #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["[■□□□□□□□□□ 10%]","[■■□□□□□□□□ 20%]", "[■■■□□□□□□□ 30%]", "[■■■■□□□□□□ 40%]",
                "[■■■■■□□□□□ 50%]", "[■■■■■■□□□□ 60%]", "[■■■■■■■□□□ 70%]", "[■■■■■■■■□□ 80%]",
                "[■■■■■■■■■□ 90%]", "[■■■■■■■■■■ 100%]"]

    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print(message_2)
    

if __name__ == '__main__':
    # view_calendar(1)
    # file_update(1)
    b = main_clinic()
    # volunteer.volunteer(b)