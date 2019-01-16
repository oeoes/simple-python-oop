import re


class Validation:

    # validate email using regular expression
    # valid email consist of start with any chars+@+any chars+.+any chars with length 2 or three
    # example: oeoesroy@gmail.com or oeoesroy@gmail.id will be accepted
    @staticmethod
    def validate_email(email):
        if re.match(r'\w+@\w+\.\w{2,3}', email, flags=re.IGNORECASE):
            return True
        else:
            return False

    # checks if user registered or not
    def is_registered(self):
        if self.registered is True:
            return True
        else:
            return False

    # validate user's password
    # length at least 8 chars and start with Uppercase letter
    def password_constraints(self):
        if len(self.password) < 8:
            print("Password at least 8 characters.")
        elif not re.match(r'^[A-Z]', str(self.password)):
            print("Password start with uppercase")
        else:
            return True
