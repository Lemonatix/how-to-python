import numpy as np

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

list1 = [420, 50, 30]

def mw(lists):
    return sum(lists) / len(lists)

average_values = mw(values)
print(average_values)

# print(mw(values))

array = np.array([1, 2, 3, 4, 5])
mittelwert = sum(array) / len(array)
print(mittelwert)