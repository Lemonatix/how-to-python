import numpy as np
a = [3, 1, 0, -3, 9, 2, 8, 5]
b = []
ind = []

b.append(a.pop(np.argmin(a)))
b.append(a.pop(np.argmax(a)))

print(b)

for number in a:
    if int(sum(a)/len(a)) == number:
        a.pop(number)
        ind.append(number)

print(np.mean(a))
    
print(ind)