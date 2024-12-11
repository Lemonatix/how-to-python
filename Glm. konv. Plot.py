import numpy as np 
import matplotlib.pyplot as plt 

def f_n(x,n):
    return x/n

x = np.linspace(0,1,500)

n_values = [1, 2, 5, 10]

plt.figure(figsize=(8,6))
for n in n_values:
    plt.plot(x, f_n(x,n), label = f"f_n(x)=x/{n}")

plt.plot(x, np.zeros_like(x), "k--", label = "Grenzfunktion f(x) = 0")

plt.title("Funktionenfolge f_n(x) = x/n und ihre Grenzfunktion")
plt.xlabel("x")
plt.ylabel("f_n(x)")
plt.legend()
plt.grid()
plt.show()