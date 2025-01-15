import string
import random

class Hangman:
    # The initialisation function sets all member variables to default states
    def __init__(self):
        self.turn = 0
        self.playing = True
        self.words = []
        self.current_word = []
        self.failed_guesses = []
        self.correct_letters = []
        self.letters = string.ascii_lowercase[:26]

    # This new method runs the game
    def new_game(self):
        self.current_word = self.get_word()
        self.show_blanks()

        while self.playing:
            self.take_turn()
            self.show_blanks()

            if len(self.failed_guesses) == 11:
                print("\n\nGame over, you loose")
                self.playing = False

    # Method to get a random word from a list of words
    def get_word(self):
        if len(self.words) > 0:
            return self.words.pop(random.randint(0, len(self.words)-1))
        else:
            print("\n\nGame over no more words")
            self.playing = False

    # Method to fill in the letters or blanks
    def show_blanks(self):
        num_blanks = 0
        print("\nPrevious incorrect guesses: ")
        print(self.failed_guesses)

        for letter in range(0, len(self.current_word)):
            if self.current_word[letter] in self.correct_letters:
                print(" " + self.current_word[letter] + " ", end="")
            else:
                print(" _ ", end="")
                num_blanks += 1

        if num_blanks == 0:
            print("\n\nYou win!")
            self.playing = False

    # Let the user take a guess (take a turn):
    def take_turn(self):
        made_guess = False
        while not made_guess:
            guess = input("\nEnter your guess: ")
            if guess.lower() in self.failed_guesses:
                made_guess = True
                self.turn += 1
                if guess in self.current_word:
                    self.correct_letters.append(guess)
                    self.show_hang_man(len(self.failed_guesses))

    # Make a list containing a few words as a word bank
    def new_word_bank(self):
        self.words = ["apple",
                      "freezer",
                      "substantive",
                      "normative",
                      "rubble",
                      "baseless",
                      "contingent",
                      "incontinence",
                      "absolutely"]

    # Based on the number of failed guesses (turns), retrieve this item from the dict and print the hangman image
    def show_hang_man(self, turn):
        hangman = {
            1: "      \n" + "      \n" + "      \n" + "      \n" + "      \n" + "      \n" + "  __|\n",
            2: "      \n" + "      \n" + "      \n" + "      \n" + "      \n" + "    |\n" + "  __|\n",
            3: "      \n" + "      \n" + "      \n" + "      \n" + "    |\n" + "    |\n" + "  __|\n",
            4: "      \n" + "      \n" + "      \n" + "    |\n" + "    |\n" + "    |\n" + "  __|\n",
            5: "      \n" + "      \n" + "    |\n" + "    |\n" + "    |\n" + "    |\n" + "  __|\n",
            6: "      \n" + "    |\n" + "    |\n" + "    |\n" + "    |\n" + "    |\n" + "  __|\n",
            7: " ____\n" + "    |\n" + "    |\n" + "    |\n" + "    |\n" + "    |\n" + "  __|\n",
            8: " ____\n" + " |  |\n" + "    |\n" + "    |\n" + "    |\n" + "    |\n" + "    |\n",
            9: " ____\n" + " |  |\n" + "(:) |\n" + "    |\n" + "    |\n" + "    |\n" + "  __|\n",
            10: " ____\n" + " |  |\n" + "(:) |\n" + "l:l |\n" + "    |\n" + "    |\n" + "  __|\n",
            11: " ____\n" + " |  |\n" + "(:) |\n" + "l:l |\n" + "l l |\n" + "    |\n" + "  __|\n",
        }
        print(hangman.get(turn))

hangman_game = Hangman()
hangman_game.new_word_bank()
hangman_game.new_game()


