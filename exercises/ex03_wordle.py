"""Creating a wordle game."""


__author__: str = "730574218"


def input_guess(secret_word_len: int) -> str:
    guess: str = input(f"Enter a { secret_word_len } character word: ")
    while not(len(guess) == secret_word_len): # can do not(==) or !=
        guess = input(f"That wasn't { secret_word_len } chars! Try again: ") # need to reassign guess to a new word that is given as an input; otherwise, the same word will be checked again.
    return(guess) 


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks indices."""
    assert len(char_guess) == 1
    index: int = 0
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            return True
        else:
            index += 1
    return False 
