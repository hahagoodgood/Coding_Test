import sys

S = input()
alphabet_list = [-1] * 26  # Initialize list with -1 for each of 26 alphabets

# Find the first occurrence position of each alphabet in the input string
for idx, character in enumerate(S):
    # Calculate alphabet index (a=0, b=1, ..., z=25)
    alph_location = ord(character) - 97
    
    # Only update if this alphabet hasn't appeared before
    if alphabet_list[alph_location] == -1:
        alphabet_list[alph_location] = idx

# Print the first occurrence position of each alphabet
for item in alphabet_list:
    sys.stdout.write(str(item) + ' ')