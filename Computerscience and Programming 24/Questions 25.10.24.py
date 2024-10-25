class Element: # __init__ wird durchgeführt, wenn Pt exisitert
    pass

Pt = Element() # ohne Klammer: Variable, sonst: neue Instanz der Element Klasse ruft __init auf__

print(type(Pt))

print(id(Pt))



class NewClass:
    def f():
        return "boom"

print(NewClass.f())

# self kann nicht einfach in Funktionen verwendet werden