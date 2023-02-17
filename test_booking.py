import unittest
import os
import booking_system as cb
from unittest.mock import patch



class TestQuickStart(unittest.TestCase):
    @patch('builtins.input', return_value="sinmbhel022")
    def test_email_request(self,input):
        ''' 
        Tests username of student.
        '''
        expected_result = 'sinmbhel022@student.wethinkcode.co.za'
        self.assertEqual(cb.email_request(), expected_result)
    

#     def test_calendar(self):
#         '''
#         Testing if calender creds are valid
#         '''
#         creds = None
#         if os.path.exists('token.json'):
#             creds = cb.Credentials.from_authorized_user_file('token.json', cb.SCOPES)
#         self.assertTrue(cb.calendar(), creds)


if __name__ == '__main__':
    unittest.main()  