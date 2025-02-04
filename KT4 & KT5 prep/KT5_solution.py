import numpy as np
a = [3, 7 , 0, -3, 9, 2, 8, 5]
b = []
ind = []

b.append(a.pop(np.argmin(a)))
b.append(a.pop(np.argmax(a)))
print(b)

closest_index = int(np.argmin(np.abs(np.array(a) - sum(a) / len(a))))
ind.append(closest_index)

print(np.mean(a))
    
print(ind)