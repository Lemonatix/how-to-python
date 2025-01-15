import numpy as np

arr1 = np.random.randint(0, 100, size=(5, 5))

def calculation(arr):
    arr = arr.flatten()  # Ergebnis speichern
    m = sum(arr) / len(arr)  # Mittelwert
    v = sum((x - m) ** 2 for x in arr) / (len(arr) - 1)  # Varianz
    dict = {"Mittelwert": m, "Varianz": v}
    return m, v, dict # dict funktioniert hier, ist allgemein aber problematisch

print(calculation(arr1))

# als zweizeiler:
def calc(arr):
    return {"Mittelwert": sum(arr.flatten()) / len(arr.flatten()) , "Varianz": sum((x - sum(arr.flatten()) / len(arr.flatten())) ** 2 for x in arr.flatten()) / (len(arr.flatten()) - 1)}

print(calc(arr1))