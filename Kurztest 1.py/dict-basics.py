# create a dictionary
myDictionary = {
    "name": "John Doe",
    "year": 1990,
    "expertise": "data analysis"
}

print(myDictionary)

print(type(myDictionary)) # check object type

for key, value in myDictionary.items():
    print(key, ":", value)