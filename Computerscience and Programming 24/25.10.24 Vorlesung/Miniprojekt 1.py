class Element:
    def __init__(self, name: str, mass: float):
        self.name = name
        self.mass = mass

a = Element("Wasserstoff", 2.03)
b = Element("Helium", 4.12)
c = Element("Beryllium", 6.02)
d = Element("Wrongium", -3)

x = 10

def f(arg1):
    value = 3+2*arg1
    return value # value is not defined without return value

y = f(x) # if y = value: value ist ein lokale variable: sie ist außerhalb von f nicht sichtbar für den interpreter => return-Funktion notwendig
print(y)

u=f(100)
print(u)

value1 = 0
def f(arg2):
    global value1
    value1 = 3 + 3*arg2

x = 5
f(x)
print(value1)

z = 10 # falls nicht definiert: NameError
def f(arg3):
    value = 3 + 2*arg3 # wenn statt arg 3 = z: statt 43 ist Ergebnis wieder 23, da x = z
    return value

r=f(20)
print(r) # ergibt wieder 23

def f(x, m=2, a=3):
    return a + m*x

y = f(20)
print(y)