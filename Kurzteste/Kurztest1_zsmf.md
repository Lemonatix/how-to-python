Source code: 
- alle Datentypen & Datenstrukturen werden als Klassen implementiert

    relevante primitive Datentypen:
        - integers
        - floats
        - strings (Indizierung startet bei 0 für den 1. Buchstabe)
        - booleans
        - Funktionen [len(), print(), type()]
        - Variablen

    relevante Datenstrukturen:
        - lists
        - tuples
        - dictionaries
        - sets

    relevante Operatoren:
        Plus: +
        Minus: - 
        Mal: *
        geteilt: /

Konzepte sind Klassen:

``` python
class Element: # neues Klassenobjekt namens "Element"
    pass

class Schulklasse:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

s1 = Schulklasse("Max", 17)
print(s1.name, s1.age) # gibt Max 17 aus
```

Instanzen in Python sind das, was Atome für Elemente sind:

``` python
a = Element() # ruft __init__ Methode auf, um neue Instanz für die "Element" Klasse festzulegen. Der Instanz wird die Variable a zugeteilt
b = Element # Klasse wird der Variable b zu geordnet
a.name = "Helium" # Elementklasse hat keinen Attribut "Name", deshalb wird Helium hier benannt
a.mass = 4.0026
```

Bezüglich Funktionen:
``` py
x = 10
def f(argument)
    value = 5*argument
    return value 
print(f(x))
```