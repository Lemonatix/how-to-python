# syntax
'''
if not value:
    statement(s)
'''

# example "if not" with Boolean value
a = False

if not a:
    print("a is False")

# if not with string
string1 = ""

if not string1:
    print("String is empty.")
else:
    print(string1)

# if not with list
list1 = []

if not list1:
    print("List is empty.")
else:
    print(list1)

# if not with dictionary
dict1 = {} # a = dict() also works

if not dict1:
    print("Dictionary is empty.")
else:
    print(dict1)

# is not with set
set1 = set({})

if not set1:
    print("Set is empty.")
else:
    print(set1)

# is not with tuple
tuple1 = ()

if not tuple1:
    print("Tuple is empty.")
else:
    print(tuple1)