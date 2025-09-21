# File: homework1 .  py

# --- Variables and Data Types ---

a = 10
print(a)
print(type(a)) # a is an integer datatype, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) # b is a float datatype, a number that has a decimal or is fractional

c = 3j
print(c)
print(type(c)) # c is a complex datatype, a number that has an imaginary part where j represents the imaginary number's units

d = "hello"
print(d)
print(type(d)) # d is a string datatype, text that's surrounded by quotation marks

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list datatype, an ordered sequence of items seperated by commas

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary datatype; it stores data values in pairs

g = (1, 2)
print(g)
print(type(g)) # g is a tuple datatype, an ordered sequence of elements used to store multiple items in a single variable; list elements can be changed while tuples can't after creation

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list datatype, an ordered sequence of items seperated by commas

i = True
print(i)
print(type(i)) # i is a boolean datatype; they represent two values, either True or False 

j = None
print(j)
print(type(j)) # j is a NoneType datatype; they return for the value "None", representing the absence of a value

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list datatype, an ordered sequence of items seperated by commas

l = str(14)
print(l)
print(type(l)) # l is a string function, used to convert objects into its string representation

m = 1e4
print(m)
print(type(m)) # m is a float datatype, a number that has a decimal, is fractional, or is in scientific notation using e to type the power

# 3.1 Questions
# 1) I found 9 different data types.
# 2) 
# - Integer
# - Float
# - Complex
# - String
# - List
# - Dictionary
# - Tuple
# - Boolean
# - Nonetype
# 3) List includes the variables “[1, 2, 3]”, “["apple", "banana", "strawberry"]”, and “[True, "blue", 12]”. String includes the string data type “”hello”” and the function “str(14)” that turns objects into its string representation. Float includes the variables “1.5” and “1e4”.
# 4) lt was a string. It’s not an integer because str() converts the variable into its string representation. If only 14 was inputted, then it would be an integer. 

n = {"lychee", "apple", "peach"}
print(n)
print(type(n)) # n is a set, an unordered collection of unique elements

print(10 > 9) # True, 10 is greater than 9
print(10 == 9) # False, 10 does not equal 9
print(10 <= 9) # False, 10 is not less than or equal to 9
print(bool("abc")) # True, a string exists so it evaluates to true
print(bool(123)) # True, 123 is a non-zero integer
print(bool(["apple", "cherry", "banana"])) # True, the list isn't empty so it evaluates to true
print(bool(True)) # True, "True" is already a boolean value so it returns true 
print(bool(False)) #False, "False" is already a boolean value so it returns false
print(bool(0)) # False, 0 is a not a non-zero integer so it returns false
print(bool("")) # False, it is empty so it returns false
print(bool(" ")) # True, it isn't empty because it still contains spaces
print(bool(())) # False, it is empty so it returns false
print(bool([])) # False, it is empty so it returns false
print(bool({})) # False, it is empty so it returns false
print(bool(True and False)) # False, both inputs need to be true to evaluate to true
print(bool(True and True)) # True, both inputs are true so it evulates to true
print(bool(False and False)) # False, both inputs are false so it evulates to false
print(bool(True or False)) # True, one of the inputs needs to be true so it evaulates to true
print(bool(True or True)) # True, only one of the inputs needs to evaulate to be true and in this case, both are
print(bool(False or False)) # False, one input needs to be false and both are false so it evaulates to false
print(bool(not(False))) # True, booleans only have two values so whatever isn't false is true
print(bool(not(True))) # False, booleans only have two values so whatever isn't true is false

# 1) In general, there are a lot more expressions returning true since false typically returns with empty or non-zero inputs which is less common. 
# 2) The one that surprised me the most was “bool(“ “). I thought it would return false but python doesn’t consider spaces as empty. 
# 3) Bool (abc123) -> this returns as true because an input exists and inside the parentheses isn’t empty
# 4) Print (90 >= 100) -> this returns as false because 90 isn’t greater than or equal to 100, it’s less than. 

print(10 + 5) # 15, + performs addition
print(10 - 5) # 5, - performs subtraction
print(2 * 4) # 8, * performs multipulcation
print(6 / 3) # 2.0, / performs division
print(5 % 2) # 1, % calculates the remainder when dividying the first digit by the second digit
print(3 ** 2) # 9, ** performs exponentials aka puts the first number to the power of the second number
print(15 // 2) # 7, // performs floor division which rounds the result down to the nearest integer
print(5 == 2) # False, == comapres the two values and determines whether they're equal or not
print(10 != 10) # False, != checks whether the two values are different from each other 
print(2 < 5) # True, < checks if the first value is less than the second value
print(12 > 5) # True, > checks if the first value is greater than the second value
print(5 <= 6) # True, <= checks if the first value is less than or equal to the second value
print(1 >= 10) # False, >= checks if the first value is greater than or equal to the second value
x = 5
x += 5
print(x) # 10, += adds to the variable
x -= 4
print(x) # 6, -= minuses from the variable
x *= 3
print(x) # 18, *= multiplies the variable

# 1) The operator “and” checks if both conditions are true. 
# Print (5>4 and 9>5) -> true
# Print (5<4 and 9<5) -> false
# 2) The operator “or” checks if one of the conditions are true. If at least one is true, it evaluates to true. 
# Print (5>4 or 9<5) -> true
# Print (5<4 or 9<5) -> false
# 3) The operator “not” inverts the true value so True turns into False and vice versa.
# print (not(True))
# print (not(False))

# 1) / performs division while // performs floor division which rounds the answer down which is useful if the quotient is not an integer.
# 2) % calculates the remainder which is useful for checking if a number is even or odd while // returns the rounded down quotient. 
# 3) You would use modulo (%) instead of floor division since that would give you the quotient while % gives the remainder. For example “print (15 % 4)” results in 3 since 12/3 = 4 and 3 is the remainder. 
# 4) Assignment operators assign a variable to an object. For example, you can assign x to the number 5 by typing “x = 5” and you can then use x instead of 5 in future cases. 

my_string = "hello"
print (my_string) # prints: hello
print (my_string[0]) # prints: h (the first letter)
print (my_string[1]) # prints: e (the second letter)
print (my_string[2]) # prints: l (the third letter)
print (my_string[3]) # prints: l (the fourth letter)
print (my_string[4]) # prints: o (the fifth letter)
print (my_string[-1]) # prints: o (the last letter)
print (my_string[1:3]) # prints: el (the second to fourth letter but excluding the fourth one)
print (my_string[0:5:2]) # prints: hlo (the first to the sixth letter but excluding the sixth letter in steps of 2)
print(len(my_string)) # prints: 5 (the length aka how many characters in the string)
print (my_string + "goodbye") # prints: hellogoodbye
print (my_string * 7) # prints: hellohellohellohellohellohellohello

# 1) Slicing is used to extract a portion of a sequence to create new sequences containing part of the original sequence of elements.  We used slicing for “my_string[1:3]” and “my_string[0:5:2]”.
name = "Oski"
print("Hello, my name is", name)
# 2) It prints out “Hello, my name is Oski”
name = "Oski"
print(f"Hello, my name is {name}")
# 3) It prints out “Hello, my name is Oski”
# 4) The second print statement uses f-strings which embed expressions and variables directly within {} which are evaluated at runtime. They’re useful for formatting and making theses easier to read.

# cd
# changes directories. Use it to move from one folder to another
# Example: cd Desktop

# ls
# list. Use it to find the contents of directories by names
# example: ls (just type ls to see contents of current directory)

# ls -a
# list including hidden files. use it to find contents of directories by names including hidden ones
# example: ls -a (just type la -a to see contents of current directory including hidden ones)

# mkdir
# make directory. use it to make a new directory
# example: mkdir oski

# cat
# concatenate. returns the content of a directory
# example: cat homework1.py

# pwd
# prints working directory. use it to find the path of the directory you're in
# example: pwd (just type pwd to see the path of your current directory)

# cd ..
# changes from the current directory to its parent directory
# example: cd .. to change from "/c/Users/annec/python_decal_fa25/annecy" to "/c/Users/annec/python_decal_fa25"

# cd .
# changes directory to current directory which is useful to refresh the directory
# example: cd . (just refreshes the directory)

# cd ~
# changes currect directory to home directory
# example: cd ~ to change "/c/Users/annec/python_decal_fa25/annecy" to "/c/Users/annec"

# cp
# copies files and directories and creates a duplicate at a new destination
# example: cp oski

# mv 
# move. you can use it to move or rename a file or directory
# example: mv oski python_decal_fa25

# rm
# remove. you can use it to delete files or directories from file system
# example: rm oski

# clear
# clear. clears content on the terminal screen, removing the previous output and commands from view
# example: clear (you just type clear)

# grep
# global regular expression print. you can use it to search for text within files
# example: grep oski.txt

# touch
# creates an empty file
# example: touch oski

# echo
# prints text to terminal window
# echo oski

# rmdir
# removes directory
# rmdir oski

# 2) Ls shows the contents of a directory but not the hidden files while ls -a shows the contents including the hidden files.
# 3) Hidden files are files that exist but don’t appear when listing and are hidden from view but can be seen if necessary. They are important to prevent accidental modification or deletion and create privacy. 

# ls -l
# lists contents including more information such as size and modification date
# just type ls -l out to see long format contents

# rm -r
# deletes a directory instead of just a file
# rm -r oski

# cp -r
# copies a directory
# cp -r oski