"""Practice with lists."""


__author__ = "730574218"


my_numbers: list[float] = [] # this is literal; could also do my_numbers: list[float] = list(), which is a constructor

#print(my_numbers)

# String Analogy
# my_name: str = "" # literal
# my_name: str = str() # constructor

my_numbers.append(1.5) # adds 1.5 to my list; only does one value at a time, but can do while loop for it
my_numbers.append(2.3)

#print(my_numbers) # prints only what's already been appended


game_points: list[int] = [102, 86, 94] # already populated list

#print(game_points)
# not for now, but can do multiple types in one list by doing [int | float]

#print(game_points[2]) # prints out 94
last_game: int = game_points[2] # creates local variable equal to 94, the game_points at index 2
#print(last_game)

game_points[1] = 72 # modifies list to change 86 (at index 1) to the value of 72
#print(game_points)

#class_num: str = "110"
#class_num[0] = "2" # can't do with strings what we did with lists; will return TypeError
# lists are mutable, but strings are immutable

len(game_points) # gives length of the list; 3 for game_points because there are 3 objects in list

game_points.pop(1) # removes 72 (item at index 1) 
#print(game_points)
# be careful because removing an item may adjust indices of other items in list

def display(par: list[int]) -> None:
    index: int = 0
    while index < len(par):
        print(par[index])
        index += 1

display(game_points)