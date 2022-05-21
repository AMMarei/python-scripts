"""Diminishing interest calculator for mortgage calculations"""

def get_initial_cost():
	"""Function to get initial apartment cost, while handling invalid inputs"""
	try:
		initial_cost = int(input("Please enter initial cost: "))
	except:
		print("Invalid input, please try again.")
		initial_cost = get_initial_cost()
	return initial_cost

def get_upfront_payment():
	"""Function to get upfront payment, while handling invalid inputs"""
	try:
		upfront_payment = int(input("Please enter upfront payment: "))
	except:
		print("Invalid input, please try again")
		upfront_payment = get_upfront_payment()
	return upfront_payment

def get_years():
	"""Function to get count of payment years, while handling invalid inputs"""
	try:
		year_count = int(input("Please enter count of years interest will be paid over: "))
	except:
		print("Invalid input, please try again")
		year_count = get_years()
	return year_count

def get_interest_rate():
	"""Function to get interest rate from user"""
	try:
		interest_rate = float(input("Please enter yearly interest rate: "))
	except:
		print("Invalid input, please try again")
		interest_rate = get_interest_rate()
	return interest_rate

def print_summary(initial_cost, upfront_payment, year_count, interest_rate):
	"""Function to print a summary of all inputs"""
	print("\n")
	print("________ SUMMARY ________")
	print("Initial cost is: " + str(initial_cost))
	print("Upfront payment is: " + str(upfront_payment))
	print("Amount on which interest will be calculated is : " + str(initial_cost - upfront_payment))
	print("Interest is going to be paid over " + str(year_count) + " years, with a yearly interest of " + str(interest_rate * 100) + "%")
	print("\n")

def calculate_installments(initial_cost, upfront_payment, year_count, interest_rate):
	"""Function to calculate and print diminishing monthly installments over all payment years"""
	# Counter that will be used to print monthly interest, year by year
	current_year = 1
	remaining_cost = initial_cost - upfront_payment
	# Calculating the initial full year interest on the very first year
	yearly_interest = remaining_cost * interest_rate
	
	# Keep going as long as the tenure period hasn't reached 0
	while(year_count != 0):
		monthly_installment = (remaining_cost + year_count * yearly_interest) // (year_count * 12)
		remaining_cost = remaining_cost - (monthly_installment * 12) + yearly_interest
		year_count = year_count - 1
		yearly_interest = remaining_cost * interest_rate
		print("Year " + str(current_year) + ": " + str(monthly_installment) + " monthly")
		current_year = current_year + 1

# Main starts here
if __name__ == "__main__":
	# Get inputs from user by invoking methods
	initial_cost = get_initial_cost()
	upfront_payment = get_upfront_payment()
	year_count = get_years()
	interest_rate = get_interest_rate()
	# Convert interest rate to fraction
	interest_rate = interest_rate/100
	# Print a summary of all initial inputs
	print_summary(initial_cost, upfront_payment, year_count, interest_rate)
	# Calculate and print all installments
	calculate_installments(initial_cost, upfront_payment, year_count, interest_rate)
