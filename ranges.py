'''
Genereal Definition:
- a range is a sequence of integers with specified bounderies
- boundaries are start and stop, start is typically 0
- step value can be specified, default is 1
'''

# for the built-in function the general syntax is:
'''
range(stop) -> if one argument is taken
range(start, stop) -> if two arguments are taken
range(start, stop, step) -> if three arguments are taken
'''

my_range1 = range(10) # range with specific stop
print(f"Values in {my_range1}: \n{list(my_range1)}") # creates list of values in range as formatted string

# Range with start and stop values
my_range2 = range(4, 10)
print(f"Values in {my_range2}\n{list(my_range2)}")

# Range with start, stop, and step values (these can also be negative, implying reverse counting)
my_range3 = range(4, 10, 2)
print(f"Values in {my_range3}\n{list(my_range3)}")

# alternatively
print(f'Start : {my_range3.start}') # gives Start: 4
print(f'Stop  : {my_range3.stop}') # gives Stop: 10
print(f'Step  : {my_range3.step}') # gives Step: 2

# other usage
my_range4 = range(4, 9)
print(my_range4)
print(list(my_range4))

for i in my_range4:
    print(i)

my_range = range(-4, 9) # works with negative values as it does with positive ones
print(list(my_range))

myrange = range(0, 5)
# Convert range to list
mylist = list(myrange)
print(f'List  : {mylist}')

# Convert range to set
myset = set(myrange)
print(f'Set   : {myset}')

# Convert range to tuple
mytuple = tuple(myrange)
print(f'Tuple : {mytuple}')