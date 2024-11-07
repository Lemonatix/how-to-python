# create a class
class Person: # class with identifier "Person"
    name = ""
    age = 0

    def printDetails(self):
        print("\nPerson Details")
        print("Name: ", self.name)
        print("Age: ", self.age)
 
# self parameter in printDetails(self) calls class instance

# example usage
class Laptop:
    name = "My Laptop"
    processor = "Intel Core"

    @staticmethod # is a method with a class that has no access to anything else in the class
    def start():
        print("Laptop started")

    @staticmethod
    def restart(self):
        print('Laptop is restarting')

    def details(self):
        print("My Laptop name is", self.name)
        print("It has an", self.processor, "processor.")

# with an object:
laptop1 = Laptop()
laptop1.name = 'Thinkpad X1'
laptop1.processor = 'Intel Core i9'
laptop1.details()

# accessing properties and methods of class
'''
object.property
object.method([arguments])

object.property = somevalue
variable1 = object.propery
'''

# another example with another magic function: __add__()
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        real_sum = self.real + other.real
        imag_sum = self.imag + other.imag
        return ComplexNumber(real_sum, imag_sum)

c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(4, 5)
result = c1 + c2
print(f"Result: {result.real} + {result.imag}i")