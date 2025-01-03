list_1 = ["apple", "banana", "cherry"]

for item in list_1: # since we refer to list_1 in the for loop: python knows, that one item of the list is one index (here one string)
    print(item)

# loop from 0 to 4
for i in range(5):
    print(i)

# summing of numbers
numbers = [1, 2, 3, 4, 5]
total = 0

for num in numbers:
    total += num
print(total)

# for loops with range
for x in range(5, 16, 2): # range(start, stop, step)
    print(x)