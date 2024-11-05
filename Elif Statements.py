'''
if boolean_expression_1:
    statement_1
elif boolean_expression_2:
    statement(s)
else:
    statement(s)
'''

a = 6
b = 4

# simple elif example 
if a<b:
    print(a, "is less than", b)
elif a>b:
    print(a, "is greater than", b)
else:
    print(a, "is equal to", b)

# elif with multiple blocks
c = 2

if a<0:
    print(a, "is negative")
elif a==0:
    print(a, "is 0")
elif a>0 and a<5:
    print(a, "is in (0,5)")
else:
    print(a, "is equal or greater than 5")