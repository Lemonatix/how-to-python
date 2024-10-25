# Syntax of If-Statements:
''' if boolean_expression:
        statement(s)
'''

# simple example for if statement
a = 2
b = 5

if a<b:
    print(a, "is less than", b)

# if statement where boolean is false
c = 24
d = 5

if c<d:
    print(c, "is less than", d)

# compound condition
e = 2
f = 5
g = 4

# condition evaluation to anumber
if e<f and e<g:
    print(a, "is less than", b, "and", c)

h = 2
if h:
    print(h, "is not zero")

# multiple statements in if block
i = 10
if i > 2:
    print(a, "is not zero")
    print("And this is another statement")
    print("Yet another statement")

# nested statements
x = 2
if x is not 0:
    print(a, "is not zero")
    if a > 0:
        print(a, "is positive")
        if a < 0:
            print(a, "is negative")