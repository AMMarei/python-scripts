import os
import json

def file_exists(file_name):
	"""Function tha takes file name, and returns True or False based 
	on whether file exists in the same directory or not."""
	if os.path.exists(file_name) == True:
		return True
	return False

def create_json_file(file_name):
	"""Function to create an empty dict, and dump it in the JSON file
	supplied as argument to the function."""
	with open(file_name, 'w') as file_obj:
		empty_dict = dict()
		json.dump(empty_dict, file_obj)

def read_json_file(file_name):
	"""Function that takes a JSON file name, and returns the dictionary
	contained in it."""
	with open(file_name, 'r') as file_obj:
		birthday_dict = json.load(file_obj)
	return birthday_dict

def write_to_json_file(file_name, dictionary):
	"""Function that takes a json file name and a dictionary, and writes 
	the dictionary in the file."""
	with open(file_name, 'w') as file_obj:
		json.dump(dictionary, file_obj)

def print_dict_from_json(file_name):
	"""Function that prints all content in a json file."""
	print("All available entries in the format name: DD/MM/YYYY")
	with open(file_name, 'r') as file_obj:
		birthday_dict = json.load(file_obj)
		for key, value in birthday_dict.items():
			print(key + ": " + value)

if __name__ == "__main__":
	while True:
		file_name = 'birthdays.json'
		# Check if file by the name 'birthdays.json' exists in the current 
		# directory, if not, create the file.
		if(file_exists(file_name) == False):
			create_json_file(file_name)
		
		birthday_dict = read_json_file(file_name)
		
		print("Welcome to birthday dictionary.")
		# Print all content already in the file.
		print_dict_from_json(file_name)
		user_input = input("Enter a name to check birthday, 'exit' to exit, and 'new' for new entry: ")
		
		# If user inputs 'exit', break out of the while True loop.
		if user_input == 'exit':
			break
		elif user_input == 'new':
			new_key = input("Please enter a name: ")
			new_value = input("Please enter a value: ")
			# Receive the new name and birthday from user, update them in the dictionary.
			birthday_dict[new_key.lower()] = new_value
			# Update the json file by writing the updated dictionary to it.
			write_to_json_file(file_name, birthday_dict)
		# If name supplied is in dictinary, convert it to lower case, and print associated birthday.
		elif user_input.lower() in birthday_dict.keys():
			print(birthday_dict[user_input.lower()])
		else:
			print("Invalid input, please try again.")
