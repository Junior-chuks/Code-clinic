from smtplib import SMTPException
from quickstart import *


def email_verification():
        pass


def email_request():
        user_name = input("\n------------------------------------\nPlease enter your student user name:")
        print("------------------------------------")
        email = f'{user_name.lower()}@student.wethinkcode.co.za'
        return email


def list_of_vol_slot(email):
        creds = None
        if os.path.exists('token.json'):
                creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        service = build('calendar', 'v3', credentials=creds)

        now = datetime.datetime.utcnow().isoformat() + 'Z' 
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                                singleEvents=True,
                                                orderBy='startTime').execute()
        events = events_result.get('items', [])

        lis =[]
        for event in events:
                print(event["email"])
                start = event['start'].get('dateTime', event['start'].get('date'))
                emails = event["attendees"]
                date_and_time = start.split('T')
                id = event["id"]
                title = event['summary']
                if len(emails) == 1 and emails[0]['email'] == email and title.lower() == "volunteer":
                        lis.append((date_and_time[0],date_and_time[1],title,id))

        return lis,service


def slot_display(data_structure):
        print("Your Slots :\n-------------------------------------------------------")
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
        

def cancel_volunteer(data,index,service):

        print("Cancelling volunteer slot... ")
        loader_animation()
        id = data[index][3]
        service.events().delete(calendarId='primary', eventId=id).execute()
        print("The slot has been successfuly cancelled.")


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
        user_email = email_request()
        data,servicc = list_of_vol_slot(user_email)

        if len(data) > 0 :
                slot_display(data)
                indx = choose_slot(data)
                cancel_volunteer(data,indx,servicc)
        else:
                print("Sorry but you have no slots to cancel")
        return len(data)


if __name__=="__main__":
        cancel_engine()

































# lov magnum
# dislikes biscuits
# likes ferr
# likes choc cak not vani
# 1762050895
# file = []
# file.append([1,2,3,4,5])
# print(file)
# cancel_volunteer()
# email_verification()