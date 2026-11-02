# Question 4: Using the random module

# TODO: Import the random module
import random 

# TODO: Create a list of colors
colourlist = ["red", "grey", "black", "white", "green", "brown", "yellow"]

# TODO: Use a for loop to select and print 3 random colors from the list
for _ in range(3):
  print(random.choice(colourlist))