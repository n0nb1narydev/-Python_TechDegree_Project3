import random
import time
from phrase import Phrase

class Game:

    def __init__(self):
        self.lives_left = 5
        self.phrases = [
            Phrase("Prune Juice A Warriors Drink"), 
            Phrase("Live long and prosper"), 
            Phrase("Resistance is Futile"), 
            Phrase("Theres Coffee in that Nebula"), 
            Phrase("Im a Doctor not an escalator"), 
            Phrase("Today is a good day to die"), 
            Phrase("There are four lights"), 
            Phrase("Never allow family to stand in the way of opportunity"), 
            Phrase("shut up Wesley"), 
            Phrase("I am Locutus of Borg"), 
            Phrase("space the final frontier"), 
            Phrase("These are the voyages of the starship enterprise"), 
            Phrase("explore strange new worlds"), 
            Phrase("seek out new life and new civilizations"), 
            Phrase("to boldly go where no one has gone before"), 
            Phrase("you are my sunshine"), 
            Phrase("hes been seized by the pon farr"),
            Phrase("comfort is irrelevant were here to work"), 
            Phrase("please state the nature of the medical emergency"), 
            Phrase("this isnt part of my program"), 
            Phrase("i have and always shall be your friend"), 
            Phrase("hes dead jim"), 
            Phrase("tea earl grey hot"),
            Phrase("beam me up scotty"), 
            Phrase("this is highly illogical"), 
            Phrase("the needs of the many outweigh the needs of the few or the one"), 
            Phrase("infinite diversity in infinite combinations"),
            ]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]
        self.phrase_complete = False

    def game_intro(self):
        print("          ______ _______ ______ ______    _______ ______  ______ __  __\n         / __  //__  __// __  // __  /   /__  __// __  / / ____// / / /\n        / / /_/   / /  / /_/ // /_/ /      / /  / /_/ / / /__  / //'/'\n        _\ \     / /  / __  //   __/      / /  /   __/ / __ / /  '/'\n      / /_/ /   / /  / / / // /\ \       / /  / /\ \  / /___ / /\ \ \n     /_____/   /_/  /_/ /_//_/  \_\     /_/  /_/  \_\/_____//_/  \_\ \n\n                         P H R A S E  H U N T E R\n\n     .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.\n:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\ \n'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'      `\n\n")
        print("                              N- New Game\n                              Q- Quit\n\n")
        self.option = None
        while self.option != "N" or self.option != "Q":
            try:
                self.option =input("Press 'N' to start a new game or 'Q' to quit: ")
            except ValueError:
                self.option =input("Press 'N' to start a new game or 'Q' to quit: ")
            else:
                if self.option.upper() == 'N':
                    self.start()
                    break
                elif self.option.upper() == 'Q':
                    print("Thank you for playing!")
                    break

    def get_random_phrase(self):
        self.num = random.randrange(0, 27)
        return self.phrases[self.num]

    def start(self):
        play_again = "Y"
        while play_again.upper() == "Y":
            while(self.lives_left > 0 and not self.active_phrase.check_complete(self.guesses)):
                print(f"Lives Left: {self.lives_left}\n\n")
                self.active_phrase.display(self.guesses)
                try:
                    self.user_guess = self.get_guess()
                    if len(self.user_guess) > 1 or not self.user_guess.isalpha():
                        raise ValueError ("Please enter one valid letter.")
                except ValueError as error:
                    print(f"({error})")
                    continue
                else:
                    self.guesses.append(self.user_guess)
                if not self.active_phrase.check_guess(self.user_guess):
                    self.lives_left -= 1
            self.game_over()
            self.reset()
            play_again = self.get_play_again()
        print("Thanks for playing!")



    def get_guess(self):
            self.user_guess = input("\n\nEnter a letter: ")
            return self.user_guess.lower()

    def game_over(self):
        if self.lives_left == 0: 
            print("\n      )      COMPUTER                                      \n     (                                                     \n      )        TEA                                         \n  _.-~(~-.                                                 \n (@\`---'/.      EARL GREY                                )\n('  `._.'  `)                                            ( \n `-..___..-'       HOT                                    )\n                                              .-.,--^--.  _\n                                              \\| `---' |//\n                                               \|        / \n                                               _\_______/_ \n\n     H A V E  S O M E  T E A  A N D  T R Y  A G A I N!\n\n")
        else:
            print(f"You guessed the phrase: {self.active_phrase.phrase}")
            print("  ____              _       _ \n / __ \            | |     | |\n| |  | | __ _ _ __ | | __ _| |\n| |  | |/ _` | '_ \| |/ _` | |\n| |__| | (_| | |_) | | (_| |_|\n \___\_\\__,_| .__/|_|\__,_(_)\n             | |              \n             |_|              \n\n         S U C C E S S!\n\n")

    def get_play_again(self):
        while True:
            play_again = input("Play Again? (Y/N) ")
            if play_again.upper() == 'Y' or play_again.upper() == "N":
                return play_again
                break
            else:
                continue


    def reset(self):
        self.lives_left = 5
        self.guesses= [" "]
        self.active_phrase = self.get_random_phrase()

