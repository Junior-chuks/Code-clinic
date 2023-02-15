from quickstart import *


def email_request():
    user_name = input("\n------------------------------------\nPlease enter your student user name:")
    print("------------------------------------")
    email = f'{user_name.lower()}@student.wethinkcode.co.za'
    return email
    