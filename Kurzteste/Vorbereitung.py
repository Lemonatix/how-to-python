import numpy as np

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

list1 = [420, 50, 30]

def mw(lists):
    return sum(lists) / len(lists)

average_values = mw(values)
# print(average_values)

# print(mw(values))

array = np.array([1, 2, 3, 4, 5])
mittelwert = sum(array) / len(array)
# print(mittelwert)

list0 = [34, 13, 3, 21, 8, 5, 2, 1] 
# print(len(list0))
# print(np.median(list0))

def median(numbers):
    numbers.sort()
    if len(numbers) % 2 == 0:
        median1 = numbers[len(numbers) // 2]
        median2 = numbers[(len(numbers) // 2) - 1]
        median = (median1 + median2) / 2
    else:
        median = numbers[len(numbers) // 2]
    return median

list0 = [34, 13, 3, 21, 8, 5, 2, 1]
print(median(list0))

# variance from scratch
list0 = [34, 13, 3, 21, 8, 5, 2, 1]
print(np.var(list0))

def variance(numbers):
    m = sum(numbers) / len(numbers)
    var = sum((x - m)**2 for x in numbers) / len(numbers)
    return var

print(variance(list0))