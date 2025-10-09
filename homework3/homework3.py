def say_goodbye(name):
	print("Goodbye,", name)

def area(radius):
	# calculates area of a circle
	pi = 3.14
	area = pi * (radius **2)
	return area

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	return a / b

readings = [15, 14, 17, 20, 23, 28, 20]

def what_should_i_wear(readings):
	min_temp = min(readings)
	max_temp = max(readings)
	return (min_temp, max_temp)

def is_weekend(day):
	week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
	if week[day] == "Sunday" or week[day] == "Saturday":
		return "It's the weekend! :D"
	else: 
		return "It is not the weekend. :("
	
def most_fuel_efficient(miles, gallons):
	return miles / gallons

integer = 12345
def decryption(integer):
	last_digit = integer % 10 #5
	first_digit = integer // 10 #1234
	rotated_number = int(f'{last_digit}' + f'{first_digit}')
	return rotated_number

def exponent(x, y):
	answer = 1
	for i in range(y):
		answer *= x
	return answer

my_list = [213, 4324, 43, 432, 54, 87, 98, -354, 234, -5464642]

def minimum_value(my_list):
	smallest = my_list[0]
	for i in my_list:
		if i < smallest:
			smallest = i 
	return smallest

def maximum_value(my_list):
	largest = my_list[0]
	for i in my_list:
		if i > largest:
			largest = i
	return largest

def while_min_value(my_list):
	smallest = my_list[0]
	i = 0
	while i < len(my_list):
		if my_list[i] < smallest:
			smallest = my_list[i]
		i += 1
	return smallest

def while_max_value(my_list):
	largest = my_list[0]
	i = 0
	while i < len(my_list):
		if my_list[i] > largest:
			largest = my_list[i]
		i += 1
	return largest

def calculate_sum(integer):
	total_sum = 0
	for i in (f'{integer}'):
		total_sum += int(i)
	return total_sum

print(calculate_sum(12345)) # the sum of the digits in 12345
