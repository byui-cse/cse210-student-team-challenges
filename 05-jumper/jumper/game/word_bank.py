import random
# from urllib.request import urlretrieve


class Word_Bank:
    def __init__(self):
        self.rand_word = ""

    def get_random_word(self):
        words = ['amigo', 'sasquach', 'geronimo', 'butter']
        self.rand_word = words[random.randint(0, 3)]
        return self.rand_word


'''This code is for the extra

def __init__(self):
    self.url = 'https://www.mit.edu/~ecprice/wordlist.10000'

def urlretrieve(url, words):
    words = '''
