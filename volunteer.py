
import os.path
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import datetime


SCOPES = ['https://www.googleapis.com/auth/calendar']


def clinic_cred():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    return creds
    

def student_cred():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('tokens.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    return creds


def calendar(cred):
    service = build('calendar', 'v3', credentials=cred)
    return service


def volunteer(cred):

    service = calendar(cred)
    current_time = datetime.datetime.now().strftime("%H:%M")
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    time_split = current_time.split(":")

    user_name = input("Student user name: ")
    email = f'{user_name.lower()}@student.wethinkcode.co.za'
    title = input("Please type 'volunteer: ")
    location = input("Location: ")
    description = input("What do you want help with? ")
    date = input("Start date(yy-mm-dd): ")
    date_0 = input("End date(yy-mm-dd): ")

    while True:
        time = input("Time(00:00): ")
        hour = time.split(":")
        if time_split[0] == hour[0] and time_split[1] >= hour[1] and date == current_date or hour[0] < time_split[0] and current_date == date:
            print("This time has already passed.")
            continue
        break

    complete_date = f'{date_0}T{hour[0]}:{hour[1]}:00+02:00'
    lis_dates = slot_time(service)

    if (complete_date,email) not in lis_dates :
        if hour[1] == "30":
            hour[1] = "00"
            if hour[0] == "23":
                hour[0] = "00"
            else:
                hour[0] = str(int(hour[0])+ 1)
        elif hour[1] == "00":
            hour[1] = "30"
        
        else:
            hour[1] = str(int(hour[1])+30)
            if int(hour[1]) > 60:
                hour[1] = str(int(hour[1])-60)
                hour[0] = str(int(hour[0])+1)

        event = {
        'summary': title,
        'location': location,
        'description': description,
        'start': {
            'dateTime': f'{date}T{time}:00+02:00',
            'timeZone': 'Africa/Johannesburg',
        },
        'end': {
            'dateTime': f'{date_0}T{hour[0]}:{hour[1]}:00+02:00',
            'timeZone': 'Africa/Johannesburg',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT=1'
        ],
        'eventType':"focusTime",
        'attendees': [
            {'email': email},
            
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
            ],
        },
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        print ('Event created: %s' % (event.get('htmlLink')))

    else :
        print("This time is already taken.Please choose another.")


def slot_time(serv):
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        
    events_result = serv.events().list(calendarId='primary', timeMin=now,
                                            singleEvents=True,
                                            orderBy='startTime').execute()
    events = events_result.get('items', [])

    lis_dates = []
    for event in events:
        lis_dates.append((event['start'].get('dateTime', event['start'].get('date')),event["attendees"][0]["email"]))
    return lis_dates


def slot_checker():

    c = clinic_cred()
    volunteer(c)


if __name__ == "__main__":
    
    slot_checker()
    # print(slot_time(calendar(clinic_cred())))