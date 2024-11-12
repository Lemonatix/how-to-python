fib_reihe = [1,1]
for i in range (100):
    fib_reihe.append(fib_reihe[-1] + fib_reihe[-2])

print(fib_reihe)

for i in range(25): # gibt gerade Zahlen bis 0 bis 50
    print(i*2)

for i in range(25): # gibt ungerade Zahlen von 0 bis 50 aus
    print(i*2+1)

print(fib_reihe[-1]/fib_reihe[-2]) # gibt den goldenen Schnitt raus 
