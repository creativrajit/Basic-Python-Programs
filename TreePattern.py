# Let's make a tree pattern
'''
    #
   ###
  #####
 #######
#########
'''

# Input tree_height from user
tree_height = eval(input("How tall is the tree?: "))


# Initialize required variables
num_of_spaces = tree_height -1
num_of_hashes = 1

# Loop the program  5 times
for counter in range(tree_height):

    # Print out hashes
    print(" " * num_of_spaces + "*" * num_of_hashes)

    # Increment hashes Decrement space
    num_of_spaces -= 1
    num_of_hashes += 2

for i in range(3):
    print(" " * (tree_height - 1) + "#")



