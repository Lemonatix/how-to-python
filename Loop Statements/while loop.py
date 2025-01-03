# example with list
list_1 = ["apple", "banana", "cherry"]

index = 0 
while index < len(list_1): # since index = 0 which is smaller then the length of the list, the whole list gets printed
    print(list_1[index])
    index += 1

# simples counter
count = 0

while count < 5:
    print("Count is:", count)
    count +=1

# break out of loop, when condition is met
number = 0

while True:
    number += 1
    print("Current number:", number)
    
    if number == 5:
        print("Number is 5, breaking the loop.")
        break

# keep track of attempts
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    # Here, you could ask the user for a guess or do something else
    print("Attempt", attempts + 1, "of", max_attempts)
    attempts += 1

print("Out of attempts!")


# user input until condition is met: Password validation with error messages
password = ""

while password != "secret":
    password = input("Enter password: ")  # Correct syntax for assigning input to the variable

    if password == "sicrit":
        print("Hint: You're getting closer, but 'abc' is not the password!")
    elif password != "secret":
        print("Error: Incorrect password. Please try again.")

print("Access granted!")