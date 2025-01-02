# Arithmetic Operators
a = 5
b = 2
print('a + b  :', (a + b))  #Arithmetic Addition
print('a - b  :', (a - b))  #Arithmetic Subtraction
print('a * b  :', (a * b))  #Arithmetic Multiplication
print('a / b  :', (a / b))  #Arithmetic Division
print('a % b  :', (a % b))  #Arithmetic Modular Division
print('a // b :', (a // b)) #Arithmetic Floor Division
print('a ** b :', (a ** b)) #Arithmetic Exponentiation

# Comparison Operators
a = 5
b = 2
print('a == b :', (a == b)) #Comparison Equal to
print('a != b :', (a != b)) #Comparison Not Equal to
print('a > b  :', (a > b))  #Comparison Greater than
print('a < b  :', (a < b))  #Comparison Less than
print('a >= b :', (a >= b)) #Comparison Greater than or Equal to
print('a <= b :', (a <= b)) #Comparison Less than or Equal to

# Logical Operators
a = True
b = False
print('a and b :', (a and b))
print('a or  b :', (a or b))
print('  not a :', (not a))

# Identity Operators
a = [5, 8]
b = [5, 8]
c = a
if a is b: # is identity operator
	print('a is b')
else:
	print('a is not b')

if a is not c: # is not identity operator
	print('a is not c')
else:
	print('a is c')
	
# Membership Operators
a = 'apple'
b = ['apple', 'banana', 'cherry']
print('a in b     :', (a in b))     #membership in
print('a not in b :', (a not in b)) #membership not in

# Bitwise Operators
a = 5
b = 2
print('a & b  :', (a & b))  #bitwise AND
print('a | b  :', (a | b))  #bitwise OR
print('a ^ b  :', (a ^ b))  #bitwise XOR
print('  ~ b  :', (~ b))    #bitwise NOT
print('a << b :', (a << b)) #bitwise Left Shift
print('a >> b :', (a >> b)) #bitwise Right Shift