import validation as v
import token as t


# Handling account registration by inherit Validation class and Token Class
class Account(v.Validation, t.Token):

    session = False
    registered = False
    active_users = 0

    # specify user's data through instantiation
    def __init__(self, first_name, last_name, email, password, address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.address = address

    # register the inserted data from instance
    # email and password will be validated. See Validation Class
    def register(self):
        if not Account.validate_email(self.email):
            return "Invalid email"
        elif self.password_constraints() is not True:
            return self.password_constraints()
        else:
            self.registered = True
            print("Welcome {}!, your account has been created.".format(self.first_name))

    # login user after registered, by look at registered variable value True/False
    def login(self, email, password):
        if self.is_registered() is False:
            print("Your account not registered yet.")

        elif email is self.email and password is self.password:
            # create session
            self.session = True

            # create token. See Token class
            self.generate_token()

            # determining how many active/login users
            Account.active_users += 1

            print("Welcome {name}! You're logged in, your To"
                  "ken is: {token}.".format(name=self.first_name, token=self.retrieve_token()))
        else:
            # raise NameError('Invalid Credentials')
            print("Sorry, invalid credentials :(")

    # logout user, token will be erased and session will be turned into False
    def logout(self):
        self.token = []
        self.session = False

        print("You're logged out!")


oeoes = Account('Oeoes', 'Roy', 'oeoesroy@gmail.com', 'A12345678', 'Jakasampurna')
uus = Account('Uus', 'Rusdiana', 'uusr@yahoo.com', 'Uus123456', 'Galaxy Bimasakti')

oeoes.register()
oeoes.login('oeoesroy@gmail.com', 'A12345678')
print()

uus.register()
uus.login('uusr@yahoo.com', 'Uus123456')
print()

print("Token: {}".format(uus.retrieve_token()))
uus.logout()
uus.retrieve_token()
print("Active user: {}".format(Account.active_users))
print("Token: {}".format(uus.retrieve_token()))
