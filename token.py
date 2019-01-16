import random as r


class Token:

    # collect randomize char form random.choice() function
    token = []

    # generate token from char collection in random_str variable
    def generate_token(self):
        random_str = list("0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
        token_creation = []
        for i in range(20):
            token_creation.append(r.choice(random_str))

        # replace token with token_creation
        self.token = token_creation

    # return generated token and converted token from list into string
    def retrieve_token(self):
        mytoken = ""
        for i in range(len(self.token)):
            mytoken += self.token[i]

        return mytoken
