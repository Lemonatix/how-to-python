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

# list of dictionaries
myList = [
	{
		'foo':12,
		'bar':14
	},
	{
		'moo':52,
		'car':641
	},
	{
		'doo':6,
		'tar':84
	}
]
print(myList)

# Convert lists to dictionary
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']

# Convert lists to dictionary
dictionary = dict(zip(keys, values))

print(dictionary)
