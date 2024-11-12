x = 4
def myFun():
    a = x**2
    b = x*2
    return a,b

o = myFun()
print([1])

if not 3 != 4:
    print("OMG!")

for i in range (10):
    try:
        a = 1/0
    except ZeroDivisionError:
        a = 2/0
        print("Durch 0 geteilt!")
    finally:
        print("viele Fehler")