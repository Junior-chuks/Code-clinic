from quickstart import *


def email_request():
    user_name = input("\n+------------------------------------+\n|Please enter your student user name: ")
    print("+------------------------------------+")

    name_ending = user_name[-3:]
    if name_ending == "022" and (len(user_name) == 9 or len(user_name) == 10 or len(user_name) == 11 or len(user_name) == 12) :
        email = f'{user_name.lower()}@student.wethinkcode.co.za'
        return email

    print("\nInvalid student user name, please try again.")
    email_request()


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


def choose_slot(data):
    number = int(input("Please choose a number ?"))
    if len(data) < number or number <= 0 :
            print("The number you chose is not on the list.")
            choose_slot(data)
    indx = number-1
    return indx


def booker(service,data,email):

    indx = choose_slot(data)
    id = data[indx][3]
    description = input("\nWhat do you want help with? ")
    # First retrieve the event from the API.
    event = service.events().get(calendarId='primary', eventId=id).execute()

    event['summary'] = 'Booked'
    event['description'] = description
    attnedees = event['attendees']
    attnedees.append({"email":email})

    updated_event = service.events().update(calendarId='primary', eventId=event['id'], body=event).execute()

    # Print the updated date.
    # print (updated_event['updated'])
    print("Slot successfully booked")


def booking_engine():
    email = email_request()
    serv = calendar()
    data = list_of_vol_slot(email,serv)
    if len(data) > 0 :
        slot_display(data)
        booker(serv,data,email)
    else:
        print("Sorry but you have no available slots to book. :(")
        return len(data)


if __name__=="__main__":
    booking_engine()
    