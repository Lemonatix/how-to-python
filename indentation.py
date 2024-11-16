def myFunction():
    print("hello")
    print("hello world") # this is correct, if both prints have different identation, an error occures
    
def myFunction():
  print('hello')
  print('hello world')

def myOtherFunction():
          print(1)
          print(2) # multiple indentations are possible 

a=2

if a == 2:
    print("a is equal to 2")
    if a % 2 == 0:
        print("a is even") # 2 Statements, both in an if argument
