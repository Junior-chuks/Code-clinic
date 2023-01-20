import unittest
import quickstart
from datetime import date 
from io import StringIO
from unittest.mock import patch
import sys



class TestViewCalendar(unittest.TestCase):
    
    def test_end_month_monitor(self):
        ''' Tests output of function that it returns a tuple.'''

        day = 1
        lis_day = [2] #what determines the length of the list? ...Write(implement) a test function
        today = date.today() #Returns the current local date

        list_date = str(today).split("-") #convert date to string and split to a list
        self.assertEqual(quickstart.end_month_monitor(day,lis_day,list_date),(2,8,[2,1,2,3,4,5,6,7]))


if __name__=="__main__":
    unittest.main()