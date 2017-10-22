users_lists = {'glo@gmail.com': {'name': 'gilo', 'email': 'glo@gmail.com', 'password': 'gggggg'}}

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
            if email not in users_lists.keys():
                if password == cpassword:
                    if len(password) >= 6:
                        users_lists[email] = {'name': name,'password': password}
                        print (users_lists)
                        return 1 #success,login page
                    else:
                        return 12
                else:
                    return 2 #Password dont match
            else:
                return 3 #Email already registred
        else:
            return 4 #Fill in all the fields

    def login(self, email, password):
        """ Login method"""
        if email != ''and password != '':
            if email in users_lists.keys():
                if password == users_lists[email]['password']:
                    return 5 #Login successfull
                else:
                    return 6 #Wrong password
            else:
                return 7 #Invalid Email
        else:
            return 4 #Fill in all the fields

    def resetpassword(self, name, email, npassword, ncpassword):
        """Reset password method """
        if email != '':
            if email in users_lists.keys():
                if npassword == ncpassword:
                    users_lists[email] = [name, npassword]
                    return "Successfully changed password"
                else:
                    return "Passwords do not match"
            else:
                return "Email not registered"
        else:
            return "Email cant be blank"
