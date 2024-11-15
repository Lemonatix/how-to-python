'''
General definition:
- used to handle exceptions that occur during the execution of a program
- when interpreter encounters error it would stop, but with try except we can check the error and handle it
'''

# general syntax
'''
try:
    statement
except:
    statement
'''

# simple example regarding zero division error
a = 3
b = 0
c = 0
try:
    c = a/b
except ZeroDivisionError: # if this would not be in the code, we get the error: 'ZeroDivisionError: division by zero'
    print('b cannot be zero')
print(c)

# extended example
x = input('Enter numenator : ')
y = input('Enter denomenator : ')

try: # for this example, enter integers in terminal
    a = int(x)
    b = int(y)
    c = a/b
except ValueError:
    print('Check if input string is parsable integer')
except ZeroDivisionError:
    print('Denomenator is zero.')
else:
    print('No Errors.')