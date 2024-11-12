# simple example for class constructor __init__()
class Laptop:
	
	def __init__(self, name, processor, ssd, ram, cost):
		self.name = name
		self.processor = processor
		self.ssd = ssd
		self.ram = ram
		self.cost = cost
		
	def details(self):
		print('The details of the laptop are:')
		print('Name         :', self.name)
		print('Processor    :', self.processor)
		print('HDD Capacity :', self.ssd)
		print('RAM          :', self.ram)
		print('Cost($)      :', self.cost)
		
#create object
laptop1 = Laptop('Thinkpad X1', 'Intel Core i9', 512, 16, 2000.00)

print(laptop1.name)
print(laptop1.processor)

laptop1.details()

# example with class destructor __del__()
# class Student is created and this object gets deleted
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self): # destroyes object
        print("Destructor called for", self.name, "age", self.age)

student1 = Student("Arjun", 14)
del student1