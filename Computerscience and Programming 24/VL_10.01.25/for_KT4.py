import numpy as np

# funktionsdefinitionen & argsort

# average from scratch
list1 = [3, 5, 7, 11, 13]
for num in list1:
    average = sum(list1) / len(list1)

print("Mean / Average is: " + str(average))    

# with numpy
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

# calculate variance

results = [-14.82381293, -0.29423447, -13.56067979, -1.6288903, -0.31632439,
          0.53459687, -1.34069996, -1.61042692, -4.03220519, -0.24332097]

print("Variance is: " + str(np.var(results)))

# from scratch variance
m = sum(results) / len(results)
var = sum((x - m)**2 for x in results) / len(results)
print("Variance is: " + str(var))

# as function
def variance(numbers):
    m = sum(numbers) / len(numbers)
    var = sum((x - m)**2 for x in numbers) / len(numbers)
    return var

data2 = [49, 60, 59, 20, 42, 36, 54, 83, 7, 8]
variance = variance(data2)
print(variance)