from smtplib import SMTPException
from quickstart import *
# lis of event and their id 
# take user email as input and match to those in  the list 
# print the ones that match 
# take a number imput of the one the user chooses to cancel
# get the id of that event and delete it
import smtplib
import random

# def email_verification():
    
#         email = input("\n-------------------------------\nplease enter your student email:")
#         print("-------------------------------")
#         num = random.randint(0,9)
#         code = [str(num) for i in range(4)]
#         complete_code = "".join(code)
#         sender = 'codeclinic123@gmail.com'
#         receivers = [email]

#         message = f"""From: From Person <codeclinic123@gmail.com>
#         To: To Person <{email}>
#         Subject: Verification code

#         {complete_code}.
#         """

#         try:
#                 smtpObj = smtplib.SMTP('smtp.gmail.com',8080)
#                 smtpObj.sendmail(sender, receivers, message)         
#                 print ("Successfully sent email\n Check your email for verification code...")
#                 smtpObj.quit()
#         except SMTPException:
#                 print ("Error: unable to send email")
        
#         return email

# def cancel_volunteer():
#         email = input("\n-------------------------------\nplease enter your student email:")
#         print("-------------------------------")

#         creds = None
#         if os.path.exists('token.json'):
#                 creds = Credentials.from_authorized_user_file('token.json', SCOPES)
#         service = build('calendar', 'v3', credentials=creds)

#         now = datetime.datetime.utcnow().isoformat() + 'Z' 
#         events_result = service.events().list(calendarId='primary', timeMin=now,
#         maxResults=7, singleEvents=True,
#         orderBy='startTime').execute()
#         events = events_result.get('items', [])
#         # service.events().delete(calendarId='primary', eventId='pvr0ntal1f352npkbpuq2btuu8_20230124T130000Z').execute()
#         lis =[]
#         for event in events:
#                 start = event['start'].get('dateTime', event['start'].get('date'))
#                 emails = event["attendees"]
#                 date_and_time = start.split('T')
#                 id = event["id"]
#                 title = event['summary']
#                 if 'volunteer' == title :

#                         print("--------------------------------------------------\n",date_and_time[0],date_and_time[1],event['summary'],emails[0]["email"],
#                         "\n--------------------------------------------------\n")
#                 print("Evaluating your selected slot...")
#                 if len(emails) == 1:
#                         if emails[0]["email"] == email :
#                                 print("Cancelling volunteer slot #########")
#                                 service.events().delete(calendarId='primary', eventId=id).execute()
#                                 print("Volunteer slot successfully cancelled...")
                        
#                         else:
#                                 print("Incorrect user of this email .Please enter your email")
#                                 cancel_volunteer()
#                 else:
#                         print("Slot cancellation was unsuccessful...\nUnfortunately you have been booked")
def email_verification():
        pass


def email_request():
        user_name = input("\n-------------------------------\nPlease enter your student user name:")
        print("-------------------------------")
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
        # service.events().delete(calendarId='primary', eventId='pvr0ntal1f352npkbpuq2btuu8_20230124T130000Z').execute()
        lis =[]
        for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                emails = event["attendees"]
                date_and_time = start.split('T')
                id = event["id"]
                title = event['summary']
                if len(emails) == 1 and emails[0]['email'] == email:
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
        if len(data) < number:
                print("The number you chose is not on the list.")
                choose_slot(data)
        indx = number-1
        return indx
        

def cancel_volunteer(data,index,service):
        id = data[index][3]
        service.events().delete(calendarId='primary', eventId=id).execute()
        print("The slot has been successfuly deleted.")



def cancel_engine():
        user_email = email_request()
        data,servicc = list_of_vol_slot(user_email)
        slot_display(data)
        indx = choose_slot(data)
        cancel_volunteer(data,indx,servicc)


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