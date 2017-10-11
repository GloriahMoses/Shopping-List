users = {}
""" Initializing a global user dict"""

class User(object):
    """
    Class for user functionionality
    """

    def __init__(self, name=None, email=None, password=None):
        """ Initializing variables"""
        self.name = name
        self.email = email
        self.password = password

    def registration(self, name, email, password, cpassword):
        """registration method"""
        if name != '' and email != ''and password != '' and cpassword != '':
            if email not in users.keys():
                if password == cpassword:
                    users[email] = [name, password]
                    return "Successfully registered"
                else:
                    return "Password dont match"
            else:
                return "Email already registred"
        else:
            return "Fill in all the fields"

    def login(self, email, password):
        """ Login method"""
        if email in users.keys():
            if password == users[email][1]:
                return "Login successfull"
            else:
                return "Wrong password"
        else:
            return "Email not registered"

    def resetpassword(self, name, email, npassword, ncpassword):
        """Reset password method """
        if email != '':
            if email in users.keys():
                if npassword == ncpassword:
                    users[email] = [name, npassword]
                    return "Successfully changed password"
                else:
                    return "Passwords do not match"
            else:
                return "Email not registered"
        else:
            return "Email cant be blank"


gilo = User()
gilo.registration ("gilo", "gmacom", "ki", "ki")
gilo.login ("gmacom", "ki")

gilo.resetpassword("gilo", "gmacom", "wa", "wa")