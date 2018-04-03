
student = {'name':'Chimp', 'age':42, 'courses':['Spring Cloud','Python', 'JPA'], 1:10}

print(student['name'])

print(student[1])

print(student.get('phone'))

print(student.get('phone', 'Are you Crazy to non existent data?'))

student['phone'] = 555-555-5555

print(student.get('phone'))

student['phone'] = '555-555-5555'

print(student.get('phone'))

del student['age']

print(student)

student.pop(1)

print(student)

print(len(student))

print(student.keys())

print(student.values())

print(student.items())

for key in student:
	print(key, student.get(key))


for key, value in student.items():
	print(key, value)