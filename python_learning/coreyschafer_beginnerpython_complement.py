import coreyschafer_beginnerpython as csbp # importing the whole file and any variable in it
import sys

courses = ['History', 'Math', 'Physics', 'CompSci']

index = csbp.find_index(courses, 'Math')
print(index)
print(csbp.test)

# can do from coreyschafer_beginnerpython import * 
# has an issue, we don't know which variables came from where
# so do this instead
# from coreyschafer_beginnerpython import find_index, test
# specify the variables you want

print(sys.path) # shows paths python will look into

# what if your imported module's path changed?
# can add directory manually!!
# sys.path.append('path')

# a better way, do this
# check video!
# setting python path is editor specific

# standard library
# say we wanna grab a random value from a list of values
# functionality is already available, random module!

courses = ['History', 'Math', 'Physics', 'CompSci']

import random
random_course = random.choice(courses)
print(random_course)

import math
# say you wanna convert 90 degrees into radians
rads = math.radians(90)
print(rads)
# to convert rads to sin
print(math.sin(rads))

import datetime
import calendar
# similar modules but very different
today = datetime.date.today()
print(today)
print(calendar.isleap(2020))

import os
print(os.getcwd())
# get wd
# scan file system
# create files, delete files, etc

# we can view the location of the module
print(os.__file__)

# just for fun
import antigravity # check it out
# feel free to check out the standard library to learn some stuff



