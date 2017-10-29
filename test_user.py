import unittest
from user import User

class Test(unittest.TestCase):
    """
        Testing users
    """
    def setUp(self):
        """Setup method creating user instance"""
        self.user = User()

    #User Registration tests

    def test_registration_empty_name(self):
        """test account creation with an empty name field"""
        output=self.user.registration('glo@gmail.com','','pass','pass')
        self.assertEqual(4, output, "Please fill your name")

    def test_registration_empty_email(self):
        """test account creation with an empty email field"""
        output=self.user.registration('','gilo','pass','pass')
        self.assertEqual(4, output, "Email is missing")

    def test_registration_empty_password(self):
        """test account creation with an empty password field"""
        output=self.user.registration('glo@gmail.com','gilo','','pass')
        self.assertEqual(4, output, "Password is missing")

    def test_registration_empty_cpassword(self):
        """test account creation with an empty password field"""
        output=self.user.registration('glo@gmail.com','gilo','pass','')
        self.assertEqual(4, output, "Please confirm password")

    def test_password_is_cpassword(self):
        """test if password is cpassword"""
        output=self.user.registration('glo@gmail.com','gilo','pass456','password')
        self.assertEqual(2, output, "Password do not match")

    def test_password_length(self):
        """test if password  length"""
        output=self.user.registration('glo@gmail.com','gilo','pass','pass')
        self.assertEqual(12, output, "Password is too short")

    #User Login tests
    
    def test_login_empty_email(self):
        """Email blank"""
        output = self.user.login('','pass')
        self.assertEqual(4, output, "Email cant be blank")

    def test_login_empty_password(self):
        """Blank password"""
        output = self.user.login('glo@gmail.com','')
        self.assertEqual(4, output, "Password cant be blank")
    
    def test_email_not_registered(self):
        """Email not registered"""
        self.user.registration('glo@gmail.com','gilo','pass','pass')
        output = self.user.login('log@gmail.com','1234')
        self.assertEqual(7, output, "Email not registered")

    def test_login_wrong_password(self):
        """wrong password"""
        self.user.registration('glo@gmail.com','gilo','pass','pass')
        output = self.user.login('glog@gmail.com','1234')
        self.assertEqual(7, output, "Wrong password")

    #Email already registered
    #Successfully registered

if __name__ == "__main__":
    unittest.main()  
  