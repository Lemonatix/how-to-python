# Syntax of If-Else
'''
this is a
multi-line string and serves as a comment
'''

a = 2
b = 4

# If Else with condition True
if a<b:
    print(a, "is less than", b)
else:
    print(a, "is greater than", b)

c = 5
# If Else with condition False
if c<b:
    print(c, "is less than", b)
else:
    print(c, "is greater than", b)

# If Else with multiple conditions
if a<b:
    print(a, "is less than", b)
    if c<b:
        print(c, "is less than", b)
    else:
        print(c, "is greater than", b)
else:
    print(a, "is greater than", b)