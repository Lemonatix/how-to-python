def myFunction():
    print("hello")
    print("hello world") # this is correct

def myFunction():
    print("hello")
     print("hello world") # this is not correct and the interpreter is confused about the different indentation
    
def myFunction():
  print('hello')
  print('hello world')

def myOtherFunction():
          print(1)
          print(2) # multiple indentations are possible 


a=2

if a ==2:
    print("a is equal to 2")
    if a % 2 == 0:
        print("a is even") # 2 Statement, both in an if argument

