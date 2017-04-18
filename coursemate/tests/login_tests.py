import unittest
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from coursemate.helpers.login_helpers import acceptable_username, acceptable_password

class LoginTest(unittest.TestCase):

    def test_usernames(self):
        test_usernames = ["Amogh100", "1000Jack", "100MixLetters450", "Should&fail"," blahFAILL****", ";;;;;;;;;;!!!!$$$$"]
        expected = [True, True, True, False, False, False]
        for index, value in enumerate(test_usernames):
            self.assertEqual(expected[index], acceptable_username(value))
    
    def test_passwords(self):
        test_passwords = ["shrt", "wrong%%%%Chars", "$%%%shouldfail", "acceptable100", "shouldWORK_100"]
        expected = [False, False, False, True, True]
        for index, value in enumerate(test_passwords):
            self.assertEqual(expected[index], acceptable_password(value))
    
if __name__ == '__main__':
    unittest.main()
    
