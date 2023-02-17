import unittest
import io
import volunteer
from test_base import captured_io
from io import StringIO
import googleapiclient.discovery


class Test_Volunteer(unittest.TestCase):

    def test_calendar(self):
        
        cred = volunteer.clinic_cred()
        cal = volunteer.calendar(cred)
        
        self.assertEqual(type(cal),  googleapiclient.discovery.Resource)


    # def test_slot_time(self):
    #     cred = volunteer.clinic_cred()
    #     service = volunteer.calendar(cred)
    #     data = volunteer.slot_time(service)
    #     self.assertEqual(type(data),list)
        
        
if __name__=="__main__":
    unittest.main()