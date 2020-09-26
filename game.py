import random
from phrase import Phrase

class Game:

    def __init__(self):
        self.missed = 0
        self.phrases = [
            Phrase("Prune Juice A Warriors Drink"), 
            Phrase("Live long and prosper"), 
            Phrase("Resistance is Futile"), 
            Phrase("Theres Coffee in that Nebula"), 
            Phrase("Im a Doctor not an escalator"), 
            Phrase("Today is a good day to die"), 
            Phrase("There are four lights"), 
            Phrase("Never allow family to stand \nin the way of opportunity"), 
            Phrase("shut up Wesley"), 
            Phrase("I am Locutus of Borg"), 
            Phrase("space the final frontier"), 
            Phrase("These are the voyages of the starship enterprise"), 
            Phrase("explore strange new worlds"), 
            Phrase("seek out new life and new civilizations"), 
            Phrase("to boldly go where no one has gone before"), 
            Phrase("you are my sunshine"), 
            Phrase("hes been stricken by the pon farr"),
            Phrase("comfort is irrelevant were here to work"), 
            Phrase("please state the nature of the medical emergency"), 
            Phrase("this isnt part of my program"), 
            Phrase("i have and always shall be your friend"), 
            Phrase("hes dead jim"), 
            Phrase("beam me up scotty"), 
            Phrase("this is highly illogical"), 
            Phrase("the needs of the many outweigh\nthe needs of the few or the one"), 
            Phrase("infinite diversity in infinite combinations"),
            ]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]

    def gameintro(self):
        print("          ______ _______ ______ ______    _______ ______  ______ __  __\n         / __  //__  __// __  // __  /   /__  __// __  / / ____// / / /\n        / / /_/   / /  / /_/ // /_/ /      / /  / /_/ / / /__  / //'/'\n        _\ \     / /  / __  //   __/      / /  /   __/ / __ / /  '/'\n      / /_/ /   / /  / / / // /\ \       / /  / /\ \  / /___ / /\ \ \n     /_____/   /_/  /_/ /_//_/  \_\     /_/  /_/  \_\/_____//_/  \_\ \n\n                         P H R A S E  H U N T E R\n\n     .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.\n:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\ \n'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'      `\n\n")
        print("                              N- New Game\n                              Q- Quit\n\n")
        option =input("Press 'N' to start a new game or 'Q' to quit: ")
        if option.upper() == 'N':
            self.start()
            pass
        elif option.upper() == 'Q':
            print("Thank you for playing!")

    def get_random_phrase(self):
        self.num = random.randrange(0, 26)
        return self.phrases[self.num]

    def start(self):
        print(f"Number missed: {self.missed}\n\n")
        self.active_phrase.display(self.guesses)




# game = Game()
# print(len(game.phrases))