a = 5
b = 2

# nested if
if a==5:
    if b>0:
        print("a is 5 and", b, "is greater than 0")

# or as combined conditions
if a==5 and b>0:
    print("a is 5 and", b, "is greater than 0")

# If-Else with AND condition
c = 3
if c==5 and b>0:
    print("c is 5 and", b, "is greater than 0")
else:
    print("c is not 5 or", b, "is not greater than 0")

# elif with AND condition
d = 8
if a<0:
    print("a is less than 0")
elif a>0 and b<8:
    print("a is in (0,8)")
elif a>7 and a<15:
    print("a is in (7,15)")

