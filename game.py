import random

class Game:

    def __init__(self):
        self.missed = 0
        self.phrases = ["Prune Juice A Warriors Drink", "Live long and prosper", "Resistance is Futile", "Theres Coffee in that Nebula", "Im a Doctor not an escalator", "Today is a good day to die", "There are four lights", "Never allow family to stand \n in the way of opportunity", "shut up Wesley", "I am Locutus of Borg", "space the final frontier", "These are the voyages of the starship enterprise", "explore strange new worlds", "seek out new life and new civilizations", "to boldly go where no one has gone before", "you are my sunshine", "hes been stricken by the pon farr", "comfort is irrelevant were here to work", "please state the nature of the medical emergency", "this isnt part of my program", "i have and always shall be your friend", "hes dead jim", "beam me up scotty", "this is highly illogical", "the needs of the many outweigh\n the needs of the few or the one", "infinite diversity in infinite combinations"]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]

    def GameIntro(self):
        print("          ______ _______ ______ ______    _______ ______  ______ __  __\n         / __  //__  __// __  // __  /   /__  __// __  / / ____// / / /\n        / / /_/   / /  / /_/ // /_/ /      / /  / /_/ / / /__  / //'/'\n        _\ \     / /  / __  //   __/      / /  /   __/ / __ / /  '/'\n      / /_/ /   / /  / / / // /\ \       / /  / /\ \  / /___ / /\ \ \n     /_____/   /_/  /_/ /_//_/  \_\     /_/  /_/  \_\/_____//_/  \_\ \n\n                         P H R A S E  H U N T E R\n\n     .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.\n:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\ \n'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'      `\n\n")
        print("                              N- New Game\n                              Q- Quit\n\n")
        option =input("Press 'N' to start a new game or 'Q' to quit: ")
        if option.upper() == 'N':
            #start game
            pass
        elif option.upper() == 'Q':
            print("Thank you for playing!")

    def get_random_phrase(self):
        self.num = random.randrange(0, 26)
        return self.phrases[self.num]

# game = Game()
# print(len(game.phrases))