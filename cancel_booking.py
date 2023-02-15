from quickstart import *


def email_request():
    user_name = input("\n------------------------------------\nPlease enter your student user name:")
    print("------------------------------------")
    print("------------------------------------")
    email = f'{user_name.lower()}@student.wethinkcode.co.za'
    return email


def calendar ():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        
    service = build('calendar', 'v3', credentials=creds)

    return service