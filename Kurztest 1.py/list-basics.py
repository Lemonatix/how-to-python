# a lost look like the following
list1 = [4, 8, 7, 6, 9]
list2 = list([4, 8, 7, 6, 9]) # built in list function

'''
datatypes in lists: [string, int, float, list, set, dict, tuple, boolean]
'''

# simple example [0, 1, 2 ,3]
list3 = ["Apple", 54, 87,36, True]
print(list3)

# accessing items: we can print only one item
print(list3[0]) # prints "Apple"
print(list3[1]) # prints 54
print(list3[-1]) # prints "True"

# we can update an existing list
'''
list[index] = new_value
'''

list4 = ["apple", "banana", "cherry"]
list4[2] = "orange"
print(list4)

mylist = [] # creates an empty list
mylist = list() # also creates an empty list
print("The list is:", mylist) 
print("List length:", len(mylist)) # length of the list is 0

# we can multiply lists: [initial_value] * n
n = 10
initial_value = 0 # initial value can also be None
output = [initial_value] * n # [initial_value] = [0]
print(output)

# we can add strings to empty list by appending, regerally: list.append(item)
x = []
x.append("apple")
print(x)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
#student objects
student1 = Student('Arjun', 14)
student2 = Student('Ajay', 15)
student3 = Student('Mike', 13)
#create list with objects
x = [student1, student2, student3]
print(x)

# list of empty lists
n = 5
x = [[]] * n
print(x)

# we can craete a sublist
y = [1, 2, 3, 4, 5]
sublist = y[1:4]
print(sublist)

z = [6, 7, 8, 9]
z.reverse() # or z = z[::-1] also reverses the list
print(z)