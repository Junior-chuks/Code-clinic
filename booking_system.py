from quickstart import *


def email_request():
    user_name = input("\n------------------------------------\nPlease enter your student user name:")
    print("------------------------------------")
    email = f'{user_name.lower()}@student.wethinkcode.co.za'
    return email
    

def calendar ():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        
    service = build('calendar', 'v3', credentials=creds)

    return service


def list_of_vol_slot(email,service):

    now = datetime.datetime.utcnow().isoformat() + 'Z' 
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                            singleEvents=True,
                                            orderBy='startTime').execute()
    events = events_result.get('items', [])
    
    lis =[]
    for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            emails = event["attendees"]
            date_and_time = start.split('T')
            id = event["id"]
            title = event['summary']
            if len(emails) == 1 and emails[0]['email'] != email and title.lower() == "volunteer":
                    lis.append((date_and_time[0],date_and_time[1],title,id))

    return lis


def slot_display(data_structure):
    print("Availble Slots :\n-------------------------------------------------------")
    print("Date             |Time                   |Task")
    num = 1
    for date,time,title,id in data_structure:
            print("-------------------------------------------------------\n",str(num)+")",date,"\t","|"+time,"\t","|"+title)
            if date == data_structure[-1][0]:
                    print("-------------------------------------------------------")
            num+=1