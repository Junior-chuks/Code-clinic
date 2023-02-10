from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from volunteer import calendar, clinic_cred
from pprint import pprint

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

# def clinic_cred():
#     creds = None
#     # The file token.json stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     if os.path.exists('token.json'):
#         creds = Credentials.from_authorized_user_file('token.json', SCOPES)
#     return creds

#from create_service import get_calendar_service  #Pseudocode
import googleapiclient

def event(serv):
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        
    events_result = serv.events().list(calendarId='primary', timeMin=now,
                                            maxResults=7, singleEvents=True,
                                            orderBy='startTime').execute()
    events = events_result.get('items', [])
    #pprint(events)

    return events




if __name__ == '__main__':
    c_creds = clinic_cred()
    serv = calendar(c_creds)
    events_ = event(serv)