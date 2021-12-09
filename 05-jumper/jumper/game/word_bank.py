import urllib.request
import random

class Word_Bank:
   """
   This class gets a word from a random dictionary and then converts that
   said word to an underscore
   """
   def get_word(self):
      """
      This function gets the word from a remote dictionary
      """
      word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

      response = urllib.request.urlopen(word_site)
      text = response.read().decode()
      words = text.splitlines()

      word = random.choice(words)

      return word

   def underscore(self, word):
      """
      This takes the word from the last function and converts it to underscore 
      """
      new_word = word
      for i in range(0, len(word)):
         new_word = new_word.replace(word[i], "_ ")
      return new_word

   def make_list(self, word):
      word_list = []

      for let in word:
         word_list.append(let)
      
      return word_list