#Sets are unordered and no deplicates list

courses = {'Maths', 'Physics','Chemistry', 'Computer Sci', 'Maths'}

print(courses)

print('Maths' in courses)

cs_courses = {'Java','Angular', 'Maths', 'Computer Sci'}

print(cs_courses .intersection(courses))

print(cs_courses.difference(courses))

print(cs_courses.union(courses))

#empty Set - watch out
#empty_set = {} // BOOM..not a inbuilt method just like lists and tuples, this will create a empty dictionary
empty_set = set()