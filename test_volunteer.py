import unittest
from volunteer import volunteer as vs
from test_base import captured_io
from io import StringIO
class Test_Volunteer(unittest.TestCase):
    def test_voloteer(self):
        with captured_io(StringIO()) as (out,err):
            result_code_event = vs("primary","primary")
            #user_eve = vs(user_event)
        output = out.getvalue().strip()
        self.assertEqual('confirmed\nconfirmed', output)
if __name__=="__main__":
    unittest.main()