# general syntax
def functionName(parameters):
    statement(s)

'''
def | python keyword to define a function
functionName | name of the function, so that we can call it later
parameters | (Optional) Input to the function
statement(s) | statements to be executed
'''

# example
def add(a, b, c): # we can set default value in the parameters, i.e. c = 0
    sum = a + b + c
    return sum 

result = add(4, 8, 2)
print("Result: ", result)

# function with arbitrary arguments
def add(*args):
    result = 0
    for x in args:
        result += x
    return result

print('Sum :', add(4, 5))
print('Sum :', add(4, 5, 7))
print('Sum :', add(4, 5, 7, 1))