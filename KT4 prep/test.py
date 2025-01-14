x = y = z = "Hello World"
print(x)

w, v, b = "Apple","Banana","Cherry"
print(w)

fruits = ['apple', 'banana', 'cherry']
a, b, c = fruits
print(a)

print('Hello', 'World') # prints Hello World

a = 'Hello'
b = 'World'
print(a + b) # print HelloWorld

x = "awesome"
def myfunc():
    x = "fantastic"
myfunc()

print("Python is " + x)

k = "hi"
def myFun():
    global k
    k = "Fantastic"
myFun() # if not called k will be "hi"
print(k)

w = 5
print(type(w))

b = 5
b = float(b)
print(type(b))

o = 5.5
o = int(o)
print(type(o))

l = 3
l = complex(l)
print(type(l))

print(int(35.88)) # gives 35

print(float(35)) # gives 35.0

print(str(35.82)) # gives 35.82

print(bool(1))