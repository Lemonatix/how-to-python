import numpy as np

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

# function definition & argsort
def perzentil(daten, p):
    daten.sort()
    n = len(daten)
    pos = p / 100 * (n-1)
    unten = int(pos)
    oben = unten + 1
    if oben >= n:
        return daten[unten]
    rest = pos - unten
    return daten[unten] + rest * (daten[oben] - daten[unten])

daten = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print("25. Perzentil:", perzentil(daten, 25))
print("50. Perzentil (Median):", perzentil(daten, 50))
print("75. Perzentil:", perzentil(daten, 75))

# mode from scratch
def modus(daten):
    häufigkeit = {}
    for wert in daten:
        if wert in häufigkeit:
            häufigkeit[wert] +=1
        else:
            häufigkeit[wert] = 1
    max_häufigkeit = max(häufigkeit.values())
    moden = [k for k, v in häufigkeit.items() if v == max_häufigkeit]
    return moden

daten = [1, 2, 2, 3, 3, 3, 4, 4, 5]
print("Modus:", modus(daten))

# R^2 score
def r2_score(y, y_pred):
    mittelwert_y = sum(y) / len(y)
    ss_tot = sum((yi - mittelwert_y) ** 2 for yi in y)
    ss_res = sum((yi - yi_pred) ** 2 for yi, yi_pred in zip(y, y_pred))
    return 1 - (ss_res / ss_tot)

y = [3, 5, 7, 9, 11]
y_pred = [2.8, 5.1, 7.2, 8.9, 11.05]

print("R²-Score:", r2_score(y, y_pred))

# z-score
def z_scores(daten):
    mittelwert = sum(daten) / len(daten)
    varianz = sum((x - mittelwert) ** 2 for x in daten) / len(daten)
    std_abw = varianz ** 0.5
    return [(x - mittelwert) / std_abw for x in daten]

# example
daten = [10, 12, 23, 23, 16, 23, 21, 16]
print("Z-Scores:", z_scores(daten))