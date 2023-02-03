from smtplib import SMTPException
from quickstart import *
# lis of event and their id 
# take user email as input and match to those in  the list 
# print the ones that match 
# take a number imput of the one the user chooses to cancel
# get the id of that event and delete it
import smtplib
import random

def email_verification():
    
        email = input("\n-------------------------------\nplease enter your student email:")
        print("-------------------------------")
        num = random.randint(0,9)
        code = [str(num) for i in range(4)]
        complete_code = "".join(code)
        sender = 'codeclinic123@gmail.com'
        receivers = [email]

        message = f"""From: From Person <codeclinic123@gmail.com>
        To: To Person <{email}>
        Subject: Verification code

        {complete_code}.
        """

        try:
                smtpObj = smtplib.SMTP('smtp.gmail.com',8080)
                smtpObj.sendmail(sender, receivers, message)         
                print ("Successfully sent email\n Check your email for verification code...")
                smtpObj.quit()
        except SMTPException:
                print ("Error: unable to send email")
        
        return email

def cancel_volunteer():
        email = input("\n-------------------------------\nplease enter your student email:")
        print("-------------------------------")

        creds = None
        if os.path.exists('token.json'):
                creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        service = build('calendar', 'v3', credentials=creds)

        now = datetime.datetime.utcnow().isoformat() + 'Z' 
        events_result = service.events().list(calendarId='primary', timeMin=now,
        maxResults=7, singleEvents=True,
        orderBy='startTime').execute()
        events = events_result.get('items', [])
        # service.events().delete(calendarId='primary', eventId='pvr0ntal1f352npkbpuq2btuu8_20230124T130000Z').execute()
        lis =[]
        for eve in events:
                start = eve['start'].get('dateTime', eve['start'].get('date'))
                emails = eve["attendees"]
                date_and_time = start.split('T')
                id = eve["id"]
                title = eve['summary']
                if 'volunteer' == title :

                        print("--------------------------------------------------\n",date_and_time[0],date_and_time[1],eve['summary'],emails[0]["email"],
                        "\n--------------------------------------------------\n")
                print("Evaluating your selected slot...")
                if len(emails) == 1:
                        if emails[0]["email"] == email :
                                print("Cancelling volunteer slot #########")
                                service.events().delete(calendarId='primary', eventId=id).execute()
                                print("Volunteer slot successfully cancelled...")
                        
                        else:
                                print("Incorrect user of this email .Please enter your email")
                                cancel_volunteer()
                else:
                        print("Slot cancellation was unsuccessful...\nUnfortunately you have been booked")

def list_of_vol_slot():
        creds = None
        if os.path.exists('token.json'):
                creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        service = build('calendar', 'v3', credentials=creds)

        now = datetime.datetime.utcnow().isoformat() + 'Z' 
        events_result = service.events().list(calendarId='primary', timeMin=now,
        maxResults=7, singleEvents=True,
        orderBy='startTime').execute()
        events = events_result.get('items', [])
        # service.events().delete(calendarId='primary', eventId='pvr0ntal1f352npkbpuq2btuu8_20230124T130000Z').execute()
        lis =[]
        for eve in events:
                start = eve['start'].get('dateTime', eve['start'].get('date'))
                emails = eve["attendees"]
                date_and_time = start.split('T')
                id = eve["id"]
                title = eve['summary']
        pass
# file = []
# file.append([1,2,3,4,5])
# print(file)
# cancel_volunteer()
email_verification()

