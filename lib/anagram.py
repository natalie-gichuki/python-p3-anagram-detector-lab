# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        return [char for char in word_list if sorted(char.lower()) == sorted(self.word) and char.lower() != self.word]
        
    pass
