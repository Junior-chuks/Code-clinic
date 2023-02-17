import unittest
import cancel_volunteer
from unittest.mock import patch
from io import StringIO
import io
import builtins
import mock
from unittest.mock import MagicMock,patch




"""
TDD for cancelling a volunteer slot
"""

class Test_Cancel_Volunteer(unittest.TestCase):
        def test_cancel_volunteer(self):
            username="sizulum022"
            with mock.patch.object(builtins, 'input', lambda _: username):
                        result=cancel_volunteer.cancel_engine()
            # Test the case where the user has existing slots to cancel
                        self.assertEqual(result, 0)
            
        
        def test_email_request(self):
            username="sizulu022"
            with mock.patch.object(builtins, 'input', lambda _: username):
                results=cancel_volunteer.email_request()
            self.assertEqual(results,"sizulu022@student.wethinkcode.co.za")

          


        def test_choose_slot(self):
            # data,email = cancel_volunteer.list_of_vol_slot("sizulu")
            data=("","","","")
            with mock.patch.object(builtins, 'input', lambda _: 1):
                num = cancel_volunteer.choose_slot(data)
            self.assertEqual(num,0)



if __name__ == '__main__':
        unittest.main()