from quickstart import *


def email_request():
    user_name = input("\n+------------------------------------+\nPlease enter your student user name: ")
    print("+------------------------------------+")
    name_ending = user_name[-3:]
    if name_ending == "022" and (len(user_name) == 9 or len(user_name) == 10 or len(user_name) == 11 or len(user_name) == 12) :
        email = f'{user_name.lower()}@student.wethinkcode.co.za'
        print("------------------------------------")
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
            if len(emails) == 2 and emails[1]['email'] == email and title.lower() == "booked":
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
    
    event = service.events().get(calendarId='primary', eventId=id).execute()

    event['summary'] = 'Volunteer'
    event['description'] = "Free session"
    attnedees = event['attendees']
    attnedees.pop(1)

    print("\nCancelling booking... ")
    loader_animation()
    updated_event = service.events().update(calendarId='primary', eventId=event['id'], body=event).execute()

    print("\nBooking successfully cancelled")


k='#'
j=0
k='#'
def loader_animation():

    from time import sleep

    def fixed_space(i,array):
        g=(' '*len(str(len(array))))
        g=g.replace(' ','',len(str(int(i))))
        return g


    def ani(i,array):
        global k
        #For accessing the global variables that are defined out of the function
        global j
        per=((i+1)*100)//len(array)
        #To calculate percentage of completion of loop
        c=per//5
        #Integer division (the value 5 decides the length of the bar)
        if c!=j:
        #When ever the values of these 2 variables change add one # to the global variable k
            k+='#'

        y='['+k+'                     '+']'
        #20 empty spaces (100/5) 
        y=y.replace(' ','',len(k))
        #To make the size of the bar fixed ever time the length of k increases one ' ' will be removed
        g=fixed_space(per,array)
        #To fix at the same position
        f=fixed_space(i,array)
        print('Status : ',y,g+str(per)+'%',' ('+f+str(i+1)+' / '+str(len(array))+' ) ',end='\r')
        #That same '\r' to clear previous text
        j=c

    array = range(100)
    for i in array:
        ani(i,array)
        sleep(0.1)


def cancel_engine():
    email = email_request()
    serv = calendar()
    data = list_of_vol_slot(email,serv)

    if len(data) > 0 :
        slot_display(data)
        booker(serv,data,email)
    else:
        print("Sorry but you no bookings to cancel.")
    return len(data)


if __name__=="__main__":
    cancel_engine()


#detect wifi service by raising exceptions.TransportError(exc)