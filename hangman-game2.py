def validate_word(set_word, all_guesses):
    """
    Function to validate the list of guesses against the set word
    :param set_word: Goal of player to guess
    :param all_guesses: The list of all guesses submitted by the player
    :return: A string where correct guesses are placed in their spots
    """
    result = ""
    for letter in set_word:
        if letter in all_guesses:
            result += letter
        else:
            result += "-"
    return(result)

def input_value():
    guess = input("Guess a letter: ")
    return guess


answer = "python"
guess_list = []
current_guess = ""

while current_guess != "quit":
    current_guess = input_value()
    guess_list.append(current_guess)
    print(validate_word(answer, guess_list))







