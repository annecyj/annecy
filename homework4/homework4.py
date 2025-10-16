# ---- 3.1 List Operations ----- 
my_favorite_foods = ["popcorn_chicken", "poke", "sesame seeds", "dan dan noodles", "bread"]

print(my_favorite_foods[1])

print(my_favorite_foods[-1])

my_favorite_foods.append("pineapple_bun")

what_keeps_the_doctor_away = "apple"
my_favorite_foods.insert(0, what_keeps_the_doctor_away)

my_favorite_foods.remove("poke")

print(len(my_favorite_foods))

for food in my_favorite_foods:
    print(food.upper())

first_and_last = my_favorite_foods[0:1] + my_favorite_foods[-1:]
print (first_and_last)
"""
I encountered this error:
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
I originally wrote: print first_and_last
I forgot to add () around first_and_last. I fixed it by adding them.
"""

if "potato" in my_favorite_foods:
    print ("A Potato!")
else:
    print ("No Potato!")

# ---- 3.2 Slicing and Striding ----- 

numbers = list(range(21))

def get_first_15(numbers):
    return numbers[0:15]
print (get_first_15(numbers))

"""
I encountered this error:
SyntaxError: expected ':'
I originally wrote: def get_first_15(numbers)
I forgot to add a colon after i defined the function. I fixed it by adding :.
"""

def get_every_fifth(first_15_numbers):
    return get_first_15(numbers)[::5]
print (get_every_fifth(get_first_15(numbers)))

def reverse_and_stride(reverse_third):
    reverse_list = reverse_third[::-1]
    return reverse_list[::3]
print (reverse_and_stride(get_every_fifth(get_first_15)))

# ---- 3.31 Nested List Operations -----
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(numbers[2])
print(numbers[1][1])
numbers.append([10, 11, 12])

def sum_nested(numbers):
    sum_nested_result = 0
    for row in numbers:
        sum_nested_result += sum(row)
    return sum_nested_result
print(sum_nested(numbers))

# ---- 3.4 Create a 5x5 List -----
def five_by_five():
    number_counter = 1
    nums = []
    for i in range(5): 
        row = [] 
        for h in range(5):
            row.append(number_counter)
            number_counter += 1
        nums.append(row)
    return nums

print(five_by_five())

two_d_array = five_by_five()

def multiples_of_three(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if arr[i][j] % 3 == 0:
                arr[i][j]="?"
    return arr

"""
I encountered this error:
TypeError: list indices must be integers or slices, not list
i originally wrote: for j in array[i]:
i forgot to use the length of the range. i fixed it by adding "range(0, len(arr[i])):"

"""

print(multiples_of_three(two_d_array))

def sum_not_equal(arr):
    counter = 0
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if arr[i][j] != "?":
                counter += arr[i][j]
    return counter

two_d_array = five_by_five()
x = multiples_of_three(two_d_array)

print(sum_not_equal(x))

# ---- 4.1 Dictionary Operations -----
ages = {
    "Katie": 30,
    "Mariam": 42, 
    "Safia": 25,
    "Mira": 48
}

print(ages["Katie"])
ages["Mira"]=100
ages["Milana"]=52
del ages["Mariam"]
for key, value in ages.items():
    print(f"{key}: {value}")
print(ages.items())

print(sum_not_equal(x))


