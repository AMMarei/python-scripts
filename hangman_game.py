import random

def new_line():
	"""Function to print a new line char."""
	print("\n")

def convert_to_list(string):
	"""Function that takes string as input, and returns a list of
	the characters in the string."""
	char_list = []
	for i in range(len(string)):
		char_list.append(string[i])
	return char_list

def show_updated_word(word_list):
	"""Function that takes a word contained in a list (letter by
	letter), for example: ['a', 'b'], and returns all letters as
	a string separated by spaces."""
	word_from_list = ' '.join(word_list)
	print(word_from_list)
	new_line()

# Retrieve all words from file 'word.txt', and strips white spaces.
with open("words.txt", 'r') as file_obj:
	word_list = file_obj.readlines()
	for i in range(len(word_list)):
		word_list[i] = word_list[i].rstrip()

# Counter to keep track of how many guesses user needed.
guess_counter = 0

# Set to keep track of all letters guessed by user.
guesses_set = set()

# Generate a random word from the list of words.
random_word = random.choice(word_list)
new_line()

# Game starts here.
print("Welcome to hangman.")
new_line()

# Convert the randomly selected word into a list of chars.
random_word_list = convert_to_list(random_word)

# Create a blueprint of the word to be guessed (as a list).
guessed_word_list = ['_' for letter in random_word]
show_updated_word(guessed_word_list)

# Keep going as long as user did not guess all letters correctly.
while guessed_word_list != random_word_list:
	guessed_letter = input("Please enter a letter: ")
	guess_counter += 1
	
	# If user already guessed this letter.
	if guessed_letter.lower() in guesses_set or guessed_letter.upper() in guesses_set:
		print("You already guessed the letter " + guessed_letter)
		guess_counter -= 1
	# If letter is correct and user did not guess it before.
	elif guessed_letter.upper() in random_word_list:
		guesses_set.add(guessed_letter)
		for i in range(len(random_word_list)):
			if random_word_list[i] == guessed_letter.upper():
				guessed_word_list[i] = guessed_letter.upper()
	# If letter is incorrect and user guessed it before.
	else:
		guesses_set.add(guessed_letter)
	# Print the updated word in the format '_ X _ Y'.
	show_updated_word(guessed_word_list)

# Print the word after user gets it correctly, and the total guesses needed.
print("Correct, word is: " + random_word)
print("You needed a total of " + str(guess_counter) + " unique guesses.")
