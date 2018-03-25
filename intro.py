# Print welcome
message = "Chimp is back with Python."

message1 = """ This is 
multiple line code"""

findlen = len(message1)

print("print the word:", message)

print("print the mutiple lines of variable string:", message1)

print("print the length:", findlen)

print("print the length -1:", findlen-1)

print("print the word(s) starting at 10 and ending at whole length:",  message1[10:findlen])

print("print the word ending at 10th position:", message[:10])

print("print the word starting at 10th position:", message[10:])

print("lower() the word:", message.lower())

print ("count() how many times the word has appeared:",  message.count('message'))

print ("find() the matching word:", message.find('message'))

print ("find() the non matching word:", message.find('message1'))

print ("replace() the word:", message.replace('Chimp', 'Chimpz'))

print ("format() the String:", '{} {} - This is formatted string with concatenation!'.format(message, message1))

print("f strings demo:",  f'{message} {message1} - This is formatted string with concatenation! with f string which is used in Python 3.6+')

print("f strings demo (tip: it has to be in quotes):",  f'{message} {message1}')

print("f strings demo (another usage, tip: functions can be invoked directly):",  f'{message.upper()} {message1}')

print("dir function:", dir(message))

print("help function:", help(str.islower))
