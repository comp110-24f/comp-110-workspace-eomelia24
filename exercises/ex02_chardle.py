"""Checking the number of instances of a character in a 5-character word."""


__author__ = "730574218"


def main() -> None:
    """Calls other functions."""
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str: # need a return statement in order to have return type be str instead of None.
    """Takes a word from a user input and checks the length."""
    word: str = input("Enter a 5-character word: ")
    if len(word) == 5: # can do if as either == 5 or != 5 and adjust else statement based on that.
        return(word) # need to have something indented after an if statement.
    else:
        print("Error: Word must contain 5 characters.") # only one return statement allowed, but multiple things can be printed.
        exit() 
    # cannot have a return statement if there is already a return statement in an if or else block.  


def input_letter() -> str:
    """Takes a letter from a user input and checks the length."""
    letter: str = input("Enter a single character: ")
    if len(letter) == 1:
        return(letter)
    else:
        print("Error: Character must be a single character.")
        exit()       


def contains_char(word: str, letter: str) -> None: # word does not have to be assigned the value of input_word here; same for the parameter letter
    """Uses inputs in other functions to check for matches of letter in word."""
    print("Searching for " + letter + " in " + word)
    count: int = 0
    if word[0] == letter:
        print(letter + " found at index 0")
        count = count + 1
    if word[1] == letter: # need to use if rather than elif because otherwise it will not check each index if it finds a matching value before the end of the word.
        print(letter + " found at index 1")
        count = count + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count = count + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count = count + 1
    if word[4] == letter: # stop at index 4 because the words are 5 letters and we start at index 0.
        print(letter + " found at index 4") 
        count = count + 1
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1: # need to add elif to have "instance" instead of "instances" when count == 1.
        print("1 instance of " + letter + " found in " + word)    
    else: # needs to be else because elif would need a boolean
        print(str(count) + " instances of " + letter + " found in " + word)          


if __name__ == "__main__":
    main()