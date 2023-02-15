import unittest
import cancel_volunteer
from io import StringIO
from test_base import captured_io
import mock
import builtins


"""
TDD for cancelling a volunteer slot
"""

class Test_Cancel_Volunteer(unittest.TestCase):
        def test_cancel_volunteer(self):
                data,email = cancel_volunteer.list_of_vol_slot("sizulu")
                results = cancel_volunteer.cancel_volunteer(data,0,email)
                self.assertTrue(results)


        def test_choose_slot(self):
            # data,email = cancel_volunteer.list_of_vol_slot("sizulu")
            data=("","","","")
            with mock.patch.object(builtins, 'input', lambda _: 1):
                num = cancel_volunteer.choose_slot(data)
            self.assertEqual(num,0)


        
    
        

    


if __name__ == '__main__':
        unittest.main()