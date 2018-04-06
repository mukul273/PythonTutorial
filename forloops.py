nums = [1,2,3,4,5]

#regular
for num in nums:
	print(num)
print('-----')
#break
for num in nums:
	if num==3:
		print(num,"is found, Chimp has it!!")
		break
	print(num)
print('-----')
#continue
for num in nums:
	if num==3:
		print(num,"is found, Chimp has it!!")
		continue
	print(num)
print('-----')
#loop in loop
for num in nums:
	for letter in 'abc':
		print(num, letter)
print('-----')
#range
for i in range(10):
	print(i)

print('-----')
#range with starting position
for i in range(2, 10):
	print(i)