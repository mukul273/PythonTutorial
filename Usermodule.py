#import import_module as mymod #this aliases the module name

#directly importing only the functions as opposed to whole module

#from import_module import find_index # nothing else can be imported here

#from import_module import * #this means that import everything from that module

from import_module import find_index, test # Aha

courses = ['Python','Angular', 'Spring Cloud', 'AWS']

index = find_index(courses, 'Cloud')

print(index)

index = find_index(courses, 'Angular')

print(index, test)

import sys
print(sys.path) #environment variable

print(sys)

import random #random is a standard python library just like math

random_course = random.choice(courses)
print(random_course)

import math

rads = math.radians(90)
print(math.sin(rads))

import datetime
import calendar

today = datetime.date.today()

print(today)
print(calendar.isleap(2020))

import os
print(os.getcwd())
print(os.__file__)

import antigravity #fun