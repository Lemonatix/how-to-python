# Klasse
class Element: # nothing happens and the Element is skipped
    pass

print(type(Element))

print(dir(Element))

Element.__dict__

a = Element # assignes variable
print(type(a))
print(dir(a))

b = Element # assignes variable
print(type(b))
print(dir(b))

print(b.__dict__)
print(a.__dict__)

b.name = "Platinum"
print(b.__dict__)

print(dir(b)) # prints the directory b
print(b.name) # print b.name

a.mass = 5
c = Element()
print(c.mass)
