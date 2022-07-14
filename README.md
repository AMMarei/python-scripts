# python-scripts

- **word_guessing:**
A simple word guessing game that selects a random word from the file 'words.txt', and prompts user to input letters until they manage to guess the word correctly. In order to run properly, make sure the file 'words.txt' is in the same directory as the file 'word_guessing.py'. In order to use a different set of words, just change the content of the file 'words.txt', but make sure each word is on a separate line.

- **cows_bulls:**
A simple number guessing game. User is prompted to input a number made up of 4 digits. For every digit the user guesses correctly and also at the correct index, they get a cow. For every correct digit user guesses but at an incorrect index, they get a bull. The program prints the number of guesses needed to reach the correct number at the end.

- **birthday_database:**
A script that creates a database of birthdays using JSON. User is prompted to input a name and a birthday, the script then updates the entry in the JSON file and displays all entries available to the user. The script takes care of creating a new JSON file for the very first time it is run.

- **diminishing_interest_calculator:**
I could not find any online calculator for diminishing interests on mortgages (or loans generally) that provides the output I'm looking for, so I created this one. User is prompted to enter initial loan (mortgage) amount, upfront payment (down payment), tenure years, yearly interest rate, and then the script prints out the diminishing monthly installments for the total years of repayment. The script rejects inputs that would cause it to crash, but it does not reject logically incorrect inputs (such as a down payment that is larger than the initial loan).
