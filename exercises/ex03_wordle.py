"""Creating a wordle game."""


__author__: str = "730574218"


def input_guess(secret_word_len: int) -> str:
    """Checks an input for the correct length."""
    guess: str = input(f"Enter a { secret_word_len } character word: ")
    while not(len(guess) == secret_word_len): # can do not(==) or !=
        guess = input(f"That wasn't { secret_word_len } chars! Try again: ") # need to reassign guess to a new word that is given as an input; otherwise, the same word will be checked again.
    return(guess) 


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks for a match in the secret word."""
    assert len(char_guess) == 1 # asserts that char_guess will be only one character.
    index: int = 0 
    while index < len(secret_word): # while loop to make it repeat over each index of secret_word. It continues until index is equal to the length of secret_word because that is when every index has been checked.
        if secret_word[index] == char_guess: # checks if char_guess matches the character at the current index of secret_word. 
            return True # don't need quotation marks, bool(), etc. because True is a bool on its own. Same goes for False. 
            # can have a return statement in the if block because it is saying that there is at least one match.
        else:
            index += 1
            # can't have a return value in the else block because it will cause us to exit the function completely instead of looping over every index. 
    return False # this return value must be at the same indentation of the while block or it will prevent the while loop from occurring. This value is not reached unless none of the indices matched char_guess because the return value in the if block causes us to exit the function.


def emojified(guess: str, secret_word: str) -> str:
    """Comparing two strings: provides feedback on which letters match."""
    assert len(guess) == len(secret_word) # asserts that the length of the two strings will match.
    WHITE_BOX: str = "\U00002B1C" # in all caps because it is a constant
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    result: str = "" # need to have a local variable that is an empty string that can be filled with the boxes as each index is checked. It can then be returned at the end.
    index: int = 0
    while index < len(guess):
        if guess[index] == secret_word[index]:
            result += GREEN_BOX # adds the box to the string called result.
            index += 1
        elif contains_char(secret_word, guess[index]) == True: # have to set contains_char == to True because that is the instance we would want a yellow box to be returned.
            result += YELLOW_BOX 
            index += 1
        else: # if neither of the above are true, a white box is returned.
            result += WHITE_BOX 
            index += 1    
    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    N: int = 1
    guess: str = "" # need to declare local variable guess before the while loop in order to include it in boolean condition.
    while N <= 6 and guess != secret: # need guess != secret because otherwise the loop will not end after someone guesses correctly.
        print(f"=== Turn { N }/6 ===")
        guess = input_guess(len(secret)) # reassigns guess to the first input on the first turn and reassigns the value of guess to the future inputs on subsequent turns.
        print(emojified(guess, secret)) # emojified takes the local variable guess as the argument of its parameter guess.
        if guess == secret:
            print(f"You won in { N }/6 turns!")
        elif N == 6: # if someone is on their last turn and gets it wrong, then the statement below is returned. 
            print("X/6 - Sorry, try again tomorrow!") # must be at this indentation/in elif block because otherwise it will print every time someone guesses.   
        N += 1    


if __name__ == "__main__":
    main(secret="codes")