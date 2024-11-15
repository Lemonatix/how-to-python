'''
Why use enumerate?
Using a for loop with iterable objects only lets us access items of the iterable, but not their index. 
For while loops, a counter variable is required to keep track of the index and/or increment.

Thats why we use enumerate with for loops. We are able to acess index and item in a precise code.
'''

iterable = ["apple", "banana", "cherry"]
# with only for loop
for item in iterable:
    print(item) # this only gets us the strings of the list without index

# with while loop 
index = 0
while index < len(iterable):
    print(index, iterable[index]) # this gets us the strings of the list with index
    index += 1

# with enumerate (for list)
for index, item in enumerate(iterable): # emumerate is a built-in function, see builtin-functions.py
    print(index, item) # gives strings of list and index in consice code

# enumerate with tuple
myTuple = ('apple', 25, 'John Cena')
for index, item in enumerate(myTuple):
    print(index, item)

# enumerate with string
myString = 'Baguette'
for index, item in enumerate(myString):
    print(index, item)

# enumerate with dictionary
fruits = {'apple': 25, 'banana': 14, 'mango':48, 'cherry': 30}
for x in enumerate(fruits.items()): # .values givebs the values of the dictionary and "fruits" as argument gives names
    print(x)

# we can also manipulate the index to not start at 0 like it would usually
myList = ['apple', 'banana', 'mango', 'cherry']
enumeratedList = enumerate(myList, start=-10) # for -10 every integer is possible
for item in enumeratedList:
    print(item)