"""CQ04 Concatenation: Concatenate two strings."""


__author__ = "730574218"


def concat(par1: str, par2: str) -> str:
    """Combine par1 and par2."""
    return par1 + par2


if __name__ == "__main__": # global variables and the function call should be indented after this line to prevent it running when imported.
    word1: str = "happy"
    word2: str = "tuesday"
    print(concat(word1,word2))
