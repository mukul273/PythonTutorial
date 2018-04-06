def hello():
	#pass #this alone hold the function without any statements in it. In normal operation we want to comment it.
	return "Shhhhh, Chimp is leaning functions in Python!!"

#regular
#hello() # to run, change return to print

#interesting 
print(hello())
print(hello)
print('-----')
#utility method
print(hello().upper())
print(len(hello()))
print('-----')
#parameters
def helloChimp(greeting):
	return '{} is testing the parameterized function.'.format(greeting)

print(helloChimp('Chimp'))
print('-----')

def helloMsChimp(greeting, name='You'):
	return '{}, {} are testing the parameterized function.'.format(greeting, name)

print(helloMsChimp('Chimp'))
print(helloMsChimp('Chimp', name='Ms.Chimp'))
print('-----')
#advanced functions : This allows arbitrary number of positional or keyword arguments
def students(*args, **kwargs):
	#pass
	print(args)
	print(kwargs)

students('Maths', 'Python', name='Chimp', age=100)
print('-----')
#List
courses = ['Angular', 'Python']
#Dictionary
info = {'name': 'Chimp', 'age': 100}

# See the difference between these two
students(courses, info)

# Aha !!!
students(*courses, **info)
print('-----')
# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    # year 2017
    # month 2
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(is_leap(2020))
print(days_in_month(2018, 2))