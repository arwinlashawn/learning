import sys
import itertool
import os
import re

# review of classes (from stack overflow)
# classes contain functions (methods) and data

# __init__ is a special method called whenever you try to make
# an instance of a class. basically, initializing the object
# here, we'll initialize some data (example)

class Ball(object):

	def __init__(self):
	# let's add some data to the instance of the class
		self.position = (100, 100)
		self.velocity = (0, 0)

	# we can also add our own functions. when our ball bounces
	# its vertical velocity will be negated (no gravity in this case)
	def bounce(self):
		self.velocity = (self.velocity[0], -self.velocity[1])


# now we have a Ball class!!
# how to use it?
ball1 = Ball()
ball1
# output
<Ball object at ...>

# you wanna make use of the DATA
ball1.position # you get (100, 100)
ball1.velocity # you get (0, 0)
ball1.position = (200, 100)
ball1.position # you get (200, 100)
# remmeber, ball1 itself remain independent (values unchanged)
ball1 # you get (0, 0)

# what about the bounce() method
ball2.bounce() # parenthese important when calling methods!
ball2.velocity # you get (5, -10) 

# now onto the REAL class
# This class is derived from the built-in Exception class!
# this new exception can be raised, like other exceptions, 
# using the raise statement with an optional error message
class NotAPathError(Exception):
	def __init__(self, message):
		self.message = message
		pass
# ...and 3 more classes derived from Exception class

# on to the functions!
# usage of re module
# provides regular expression matching operations
# SIMILAR to those in Perl
# re.search(): to search for a pattern in a text
# it takes a regexp pattern and a string
# the "r" tells python that it should be treated as
# a RAW string (take it literally)

def error_finder(paths):
	if re.search(r'/', paths):
		p=paths.split('/')
		if len(p) > 7:
			# to check consistent proteinid naming
