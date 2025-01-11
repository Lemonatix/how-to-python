import numpy as np
# Varianz ausrechnen
# funktionsdefinitionen & argsort

# average from scratch
list1 = [3, 5, 7, 11, 13]
for num in list1:
    average = sum(list1) / len(list1)

print("Mean / Average is: " + str(average))    

# mit numpy
print(np.mean(list1))

# as function
def calc_average(numbers):
    return sum(numbers) / len(numbers)

data = [10, 20, 30, 40, 50]
average1 = calc_average(data)
print(average1)

# median with numpy
print(np.median(data)) 

# from scratch median
num = [8, 5, 17, 92, 36, 20]
n = len(num)
num.sort()

if n % 2 == 0:
    median1 = num[n//2]
    median2 = num[n//2 - 1]
    median = (median1 + median2) / 2
else: 
    median = num[n//2]
print("Median is: " + str(median)) 

# as function
def median_calc(number):
    n = len(number)
    number.sort()
    if n % 2 == 0:
        median1 = number[n//2]
        median2 = number[n//2 - 1]
        median = (median1 + median2) / 2
    else: 
        median = number[n//2]
    return median

data1 = [49, 60, 59, 20, 42, 36, 54, 83, 7, 8]
med = median_calc(data1)
print(med)