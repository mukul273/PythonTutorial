evennumber = 2
oddnumber = 3
floatNumber=3.14
negativeValue = -3

strNumeven= '2'
strNumodd = '3'

print(type(oddnumber))
print(type(floatNumber))

print(floatNumber/oddnumber) # division
print(floatNumber//oddnumber) #floor division
print(oddnumber//evennumber) # another example of floor division

print(oddnumber * evennumber) #multiplication

print(oddnumber**evennumber) #exponent


print(oddnumber%evennumber) # Modulus usage1
print(floatNumber%evennumber) # Modulus usage2
print(floatNumber%oddnumber)# Modulus usage3

oddnumber +=2
print(oddnumber) #short hand for addition
oddnumber *=2
print(oddnumber) #short hand for multiplication

print(abs(negativeValue)) #absolute value with negative excluded

print(round(floatNumber)) #round off the value with only 1 digit after . usage1

print(round(3.51)) #round off the value with only 1 digit after . usage2

print(round(3.51, 1)) #round off the value with only 1 digit after . usage3

print(evennumber==oddnumber)

print(oddnumber !=evennumber)

print(oddnumber>evennumber)

print(oddnumber<evennumber)

print(oddnumber>=evennumber)

print(oddnumber<=evennumber)

print(strNumeven+strNumodd)

print(int(strNumeven)+int(strNumodd))