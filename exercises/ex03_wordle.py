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
    while index < len(char_guess):
        if secret_word[index] == char_guess:
            return bool("True")
        else:
            return bool("False")
    index += 1    
       # return secret_word == char_guess
    #index += 1
    #return secret_word
   # while secret_word[index] != char_guess:
       # index += 1
        #return
   # while index < len(secret_word):
       # if char_guess == secret_word[index]:
   #     return(char_guess == secret_word[index])
   # index += 1
       #return (char_guess == secret_word[index])
