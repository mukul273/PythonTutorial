courses = ['Maths', 'Physics','Chemistry', 'Computer Sci']
soft_courses = ['Java','Python', 'AngularJS']

nums = [1,5,3,2,4,6,7]

print(courses)

print (len(courses))

print(courses[2])

print(courses[-1])

print(courses[1:3])

print(courses[:2])

print(courses[2:])

courses.append('Art')
print(courses)

courses.insert(1, 'Draw')
print(courses)

courses.insert(0, soft_courses)
print(courses)

courses.extend(soft_courses)
print(courses)

courses.remove('Java')
print(courses)

courses.pop()
print(courses)

courses.reverse()
print(courses)

soft_courses.sort()
print(courses)

soft_courses.sort(reverse=True)
print(courses)

nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

sorted_courses = sorted(soft_courses)
print(sorted_courses)

print(min(nums))

print(max(nums))

print(sum(nums))

print(min(soft_courses))

print(max(soft_courses))

print(courses.index('Python'))

print('Computer' in courses)

for course in courses:
	print(course)


for index, course in enumerate(courses):
	print(index, course)


for index, course in enumerate(courses, start=10):
	print(index, course)


course_csv = ', '.join(soft_courses)
print(course_csv)


course_hyphen = '- '.join(soft_courses)
print(course_hyphen)

new_list = course_hyphen.split('- ')
print(new_list)

#empty list - watch out
empty_set1 = list()
empty_set2 = [] #  a inbuilt method just like tuples but unlike sets