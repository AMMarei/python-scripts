import random

def generate_random_number():
	"""Function to generate a random 4 digit number, return it as string."""
	random_string = ''
	for i in range(0, 4):
		random_string += str(random.randint(0, 9))
	
	return random_string

def get_user_input():
	""" Function to get 4 digit input from user, return it as string."""
	user_input = input("Please enter a 4 digit number: ")
	if(len(user_input) != 4):
		print("Invalid input, please make sure you enter 4 digits")
		user_input = get_user_input()
	
	return user_input

cows = 0
bulls = 0
# Counter to keep track of user's gesses.
guess_counter = 0

# Generate a random string made up of 4 numbers.
random_number = generate_random_number()

while True:
	# Increment counter every time the program goes into the while loop.
	user_input = get_user_input()
	guess_counter += 1
	
	# If user guesses number and index correctly, increment cows.
	for i in range(0, 4):
		if(user_input[i] in random_number):
			if(user_input[i] == random_number[i]):
				cows += 1
			# If user only guesses number correctly (index incorrectly), increment bulls.
			else:
				bulls += 1
	# If user guesses all 4 numbers correctly (4 cows), break out of the while loop.
	if cows == 4:
		break
	else:
		print(str(cows) + " cow(s), " + str(bulls) + " bull(s)")
		cows = 0
		bulls = 0

# Print the number, and print how many guesses were needed.
print("Finally, number is indeed: " + str(random_number))
print("You needed " + str(guess_counter) + " guess(es)")
