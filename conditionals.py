language = 'Python'

if language=='Python':
	print('Condition was true')

if False:
	print('Condition was false')

if language=='C':
	print('Condition was true')	
else:
	print('No match')

if language=='C':
	print('Condition was true')	
elif language == 'Java':
	print("Language is Java")
else:
	print('No match')

# Python doesn't have switch case statements

#Boolean operations

user = "admin"
logged_in = True

if user=='admin' and logged_in:
	print("Welcome admin")
else:
	print("Please login")

if user=='admin' or logged_in:
	print("Welcome admin")
else:
	print("Please login")

if user=='admin' and not logged_in:
	print("Welcome admin")
else:
	print("Please login")


a = [1,2,3]
b = [1,2,3]
c = a
print(a == b)

print(id(a))
print(id(b))

print(a is b)

print(a is c)


condition = False

if condition:
    print('Evaluated to True')
else:
	print('Evaluated to False')


condition = None

if condition:
    print('Evaluated to True')
else:
	print('Evaluated to False')


condition = 0

if condition:
    print('Evaluated to True')
else:
	print('Evaluated to False')	


condition = 10 #basically evaluates to true (python treats non zero numbers to true)

if condition:
    print('Evaluated to True')
else:
	print('Evaluated to False')


condition = {} #Empty mappings like dictionaries evaluates to zero

if condition:
    print('Evaluated to True')
else:
	print('Evaluated to False')


	