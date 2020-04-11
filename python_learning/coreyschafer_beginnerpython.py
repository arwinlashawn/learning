# corey schafer's python tutorial for beginners
# part 2: strings - working with textual data

message = 'Hello World'

print('Hello World')
print(message)

# difference between single and double quotes
# important in the example below
message2 = 'Bobby\'s World' # escape the single quote by using a backslash
print(message2)
# or just use both single and double quotes
message3 = "Bobby's World"
print(message3)

# to create multiline string, use triple quote
message4 = """Bobby's World was a good
cartoon in the 1990s"""
print(message4)

# we can access each individual characters in the string
print(len(message)) # gives 11, including white space

# access a specific character based on index
print(message[10])

# use of slicing
print(message[0:5]) # first index inclusive, not the last index
print(message[6:]) # if you leave the right side empty, will print till the end

# methods
# difference between method and function? basically the same thing
# method is just a function that belongs to an object

# to make the string lowercase
print(message.lower())
 
# to make the string uppercase
print(message.upper())

# to count a string, give count of the string specified
# count takes an argument
print(message.count('Hello'))
print(message.count('l'))

# use find method to find starting index of a string
# method takes an argument
# if can't find it, returns -1
print(message.find('World'))

# to replace a string
message.replace('World', 'Universe') # change not registered yet
# so do this
new_message = message.replace('World', 'Universe')
print(new_message)

# how to add multiple strings and concatenate them together
# use +
greeting = 'Hello'
name = 'Michael'

message = greeting + ', ' + name + '. Welcome!'
print(message)

# but using + sign is not the best way for when working with many strings
# so it's better to use a formatted string

message = '{}, {}. Welcome!'.format(greeting, name)
print(message)
# string formatting makes it cleaner! the brackets are placeholders

# say we want the above to be an F STRING (makes code cleaner)
message = f'{greeting}, {name}. Welcome!'
# this is kinda new to Python
print(message)
# you can do extra stuff like making name uppercase
message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

# use dir()
# if we pass in variable, in this case name, will show us all attributes and methods
# that are available to you
print(dir(name))

# use of help()
# gives you description of methods and what arguments they take
print(help(str))

# say you need more info about the lower() method
print(help(str.lower))


# part 3: integers and floats - working with numeric data

num = 3
num2 = 3.14

# to see data type of an object
print(type(num)) # gives int
print(type(num2)) # gives float

# arithmetic operators
# // is floor division, drops the decimal part if any
print(3//4) # gives 0 since 3/4 is 0.75

# ** exponent
# % is modulus, gives remainder

# any integer mod 2 will either give you 0 or 1
# this concept helps you figure out whether a number if odd or even

# can use parentheses to change normal order of operation 
print(3 * 2 + 1)
print(3 * (2 + 1))

# incrementing a variable
num = 1
# how to increment the value by 1?
num = num + 1
print(num)
# shorthand available, does the same thing
num += 1
print(num)

# abs(), to get absolute value
print(abs(-3))

# round(), round the number to nearest integer value
print(round(3.5))
# can pass in second argument, round it to which decimal
print(round(3.65, 1)) # gives you 3.6 for some reason, probably
# due to banker's rounding?
# refer to https://stackoverflow.com/questions/10825926/python-3-x-rounding-behavior
# "The simple "always round 0.5 up" technique results in a slight bias 
# toward the higher number. With large numbers of calculations, this 
# can be significant. The Python 3.0 approach eliminates this issue."

# comparisons
num_1 = 3
num_2 = 2
print(num_1 == num_2) # gives False
print(num_1 != num_2) # gives True
print(num_1 > num_2)
print(num_1 < num_2)
print(num_1 <= num_2)
print(num_1 >= num_1)

num_1 = '100'
num_2 = '200'
print(num_1 + num_2) # can't add cuz num_1 and num_2 are strings

# so we need to do casting to change em from str to int
# int()
print(int(num_1) + int(num_2))


# part 4
# lists, tuples and sets

# lists have the most functionality compared to others
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)

# can apply len() to lists
# gives number of values in the list
print(len(courses))

# can pass in index of the values 
print(courses[0]) # gives history
print(type(courses[0])) # of type str

# to get the last item of list using negative indices
# instead of counting to get the last index
print(courses[-1]) # gives CompSci
print(courses[-2]) # gives Physics

# if i wanna grab first two values
# use slicing
print(courses[0:2])
print(courses[:-1]) # gives everything up to before last item
# remember, -1 not inclusive

# to add values to the list to the end
# .append()
courses.append('Art')
print(courses)

# to add values at specific location
# .insert()
courses.insert(0, 'Science')
print(courses)

courses_2 = ['Art', 'Education']
# say you wanna add courses_2 to courses list
# if you use insert, it will add the who courses 2 list 
# into courses list
# instead of insert, you wanna use extend()
courses.extend(courses_2)
print(courses)

# now how do we remove stuff
# remove() method
courses.remove('Math')
print(courses)

# to remove last value of the list
# pop()
# pop() returns the value you removed!
popped = courses.pop()
print(popped)
print(courses)

# to reverse the list
courses.reverse()
print(courses)

# to sort the list
courses.sort()
print(courses)

# both numbers and letters can be sorted by sort()

# to sort in descending order
# add the argument reverse=True
courses.sort(reverse=True)

# how to sort the list without altering the original list
# sorted()
print(sorted(courses))

# if you want the minimum value in the list
nums = [1,2,3,4,5]
print(min(nums))
# to get max value
print(max(nums))
# to get the sum
print(sum(nums))

# to get the index of a certain value
# .index()
print(courses)
print(courses.index('CompSci'))
print(courses.index('Art')) # two 'Art's, but gives the earliest one, 
# which is at index 4

# can use in for lists!
print('Art' in courses)

# can use for loop
for item in courses:
	print(item)

# can use enumerate function to access values and index
# enumerate() returns index and value!
# super useful
for index, course in enumerate(courses):
	print(index, course)
# if you don't wanna start from 0, say you want 1
for index, course in enumerate(courses, start=1):
	print(index, course)

# join() to convert list to string, join them by a specified sep
# in this case, a comma and space
course_str = ', '.join(courses)
print(course_str)

# to convert it back to list
# split() for str to list
new_list = course_str.split(', ')
print(new_list)

# tuples
# can't modify them! immutable
# uses parentheses, not brackets
# can access tuples, but not add or remove stuff etc

# sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print(cs_courses)
# order doesn't matter for sets!
# so order may change everytime you print the set
print('Math' in cs_courses) # sets are optimized for this! 
# cuz in line with the purpose of sets

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}
# how to see what the sets have in common
# use intersection()
print(cs_courses.intersection(art_courses))
# what courses are in cs but not art?
print(cs_courses.difference(art_courses))
# all courses in both sets
print(cs_courses.union(art_courses))


# how to create empty lists, tuples, sets
empty_list = [] # or list()
empty_tuple = () # or tuple()
# BUT NOT
# empty_set = {} # wrong, will create empty dictionary!
# so do 
empty_set = set()


# part 5
# dictionaries - working with key-value pairs
# key-value pairs
# key: unique identifier to get the data
# data: definition of the key (word)

student = {'name':'John', 'age': '25', 'courses': ['Math', 'CompSci']}

print(student)

# to access the name
print(student['name'])

# to access the age
print(student['age'])

# keys can be an integer too!
# replace 'name' with 1 and it's fine
 
# what happens if we try to access a key that doesn't exist
# get error message
# so use get()
print(student.get('phone')) # returns None instead of error
print(student.get('name')) # also gets the name

# how to add phone number to the student dict
student['phone'] = '555-5555'
# to update name
student['name'] = 'Jane'
print(student.get('phone'))
print(student)

# to update more than 1 key
student.update({'name': 'Jane', 'age': 26, 'phone': '666-6666'})
print(student)

# to remove age
del student['age']
print(student)
# can also use pop() to remove
age = student.pop('phone')
print(age)

# get number of keys in dict
print(len(student))
# to get some info about the dict
print(student.keys())
print(student.values())
print(student.items())
print(student)

# to loop through BOTH key and values
# need to use item()
for key, value in student.items():
	print(key, value)


# part 6
# conditionals and booleans - if, else and elif statements
if False:
	print('Conditional was True') # statement not printed since False

language = 'Python'
if language == 'Python':
	print('Conditional was True')

# to test object identity, use "is"
# check if values have the same ID
# basically if they have the same object in memory
if language == 'Python':
	print('Language is Python')
else:
	print('No match')

# use of elif statement
language = 'Java'
if language == 'Python':
	print('Language is Python')
elif language == 'Java':
	print('Language is Java')
else:
	print('No match')

# switch case statement, a way to check multiple values
# present in other languages, not in Python

# boolean operations that we can use
# and, or, not

user = 'Admin'
logged_in = False

if user == 'Admin' or logged_in:
	print('Admin Page')
else:
	print('Bad Creds')

if not logged_in:
	print('Please log in')
else:
	print('Welcome')

# so what's the difference between == and is?
# is tests if two objects are equal and are the same in memory

a = [1,2,3]
b = [1,2,3]

print(a == b)

print(a is b) # returns False, two different objects in memory
print(id(a))
print(id(b)) # notice that the ids are different, so
# is basically tests if the ids are the same
# a is b, really the same as id(a) == id(b)

# False values:
	# False
	# None
	# Zero of any numeric type
	# Any empty sequence. For example, '', (), []
	# Any empty mapping (basically empty dict). For example, {}

condition = True

if condition:
	print('Evaluated to True')
else:
	print('Evaluate to False')

# some user-defined values that are also evaluated to False, but mostly
# those mentioned above


# part 7 
# Loops and Iterations - For/While Loops

nums = [1,2,3,4,5]

for num in nums:
	print(num)

# use of break and continue keywords
# break: breaks out of the loop
# continue: moves on the next iteration of the loop

# say you wanna look for 3
for num in nums:
	if num == 3:
		print('Found!')
		break # breaks when found 3, break happens before printing 3
	print(num)

# what if we want to ignore a value, but not break the loop
for num in nums:
	if num == 3:
		print('Found!')
		continue # printed Found! instead of printing(num) and then goes
		# on to next iteration
	print(num)


# loop within a loop
for num in nums:
	for letter in 'abc':
		print(num, letter)

# say if you wanna run through a loop 10 times
# range can take two arguments, first one here specifies start index
for i in range(1, 10):
	print(i)

# while loops
x = 0
y = 0

while x < 10:
	print(x)
	x += 1 # eventually the loop will break when x >= 10
	# must have a way to break the loop or else it'll go on indefinitely

# can use break to break out of the while loop
while y < 10:
	if y == 5:
		break
	print(y)
	y += 1

# control + C to interrupt running infinite loops 


# part 8
# functions

def hello_func():
	pass # if you wanna leave the function undefined 
	# this helps to result in no error when the function is called

print(hello_func()) # the parentheses after func is to execute the function

def hello_func1():
	print('Hello Function!')

hello_func1()

# dry, a term used to mean not repeating the same thing
# same purpose in a single location i.e. function
# keep your code dry!

def hello_there():
	return 'Hello there!'

print(hello_there())

# length of a string
print(len('Test'))

# we can treat the return value just like the data that it is

print(hello_there().upper())

# say we wanna customize hello_func
def hello_func_cus(greeting):
	return f'{greeting} function.' # new string formatting technique i learned

print(hello_func_cus('Hi'))

# let's assign a default value to hello_func_customized
def hello_func_customized(greeting, name = 'You'):
	return f'{greeting} {name} function.'

print(hello_func_customized('Hi')) # this prints Hi You function.
# since you didn't specify second argument, the default, You is used as name

# args and kwargs
# args and kwargs are just conventions, use them!
def student_info(*args, **kwargs):
	print(args) # prints out tuple
	print(kwargs) # prints out dictionary

# student_info('Math', 'Art', name = 'John', age=22)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(courses, info)
student_info(*courses, **info) # observe the result difference!

# example code
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
	"""returns True for leap years, False for non-leap years"""
	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
	"""returns number of days in that month in that year"""
	if not 1 <= month <= 12:
		return 'Invalid Month'
	if month == 2 and is_leap(year):
		return 29   
	return month_days[month]


print(is_leap(2017))
print(days_in_month(2017, 2))


# part 9: import modules and exploring the standard library
print('Imported my_module...')

test = 'Test string'

def find_index(to_search, target):
	'''Find the index of a value in a sequence'''
	for i, value in enumerate(to_search):
		if value == target:
			return i

	return -1

# you can import a variable from within the same directory
# result and method to import shown in complementary file









































