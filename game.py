# Create your Game class logic in here.
class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = ['Prune Juice: A Warriors Drink','Live long and prosper','Resistance is Futile',"There's Coffee in that Nebula","I'm a Doctor not an escalator",'Today is a good day to die.','There are four lights!','Never allow family to stand \n in the way of opportunity.']
        self.active_phrase = None
        self.guesses = [" "]

    def GameIntro(self):
        print("          ______ _______ ______ ______    _______ ______  ______ __  __\n         / __  //__  __// __  // __  /   /__  __// __  / / ____// / / /\n        / / /_/   / /  / /_/ // /_/ /      / /  / /_/ / / /__  / //'/'\n        _\ \     / /  / __  //   __/      / /  /   __/ / __ / /  '/'\n      / /_/ /   / /  / / / // /\ \       / /  / /\ \  / /___ / /\ \ \n     /_____/   /_/  /_/ /_//_/  \_\     /_/  /_/  \_\/_____//_/  \_\ \n\n                         P H R A S E  H U N T E R\n\n     .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.\n:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\ \n'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'      `\n\n")
        print("                              N- New Game\n                              Q- Quit\n\n")
        option =input("Press 'N' to start a new game or 'Q' to quit: ")
        if option.upper() == 'N':
            #Start new Game
            pass
        elif option.upper() == 'Q':
            print("Thank you for playing!")


