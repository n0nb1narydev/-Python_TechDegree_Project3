# Create your Phrase class logic here.

class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses):
        for letter in phrase:
            letter.replace("_ ")
            print(f"{letter}".end = " ")
