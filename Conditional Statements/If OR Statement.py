# simple examples for if or statements

# if statement
today = "Samstag"
if today == "Samstag" or today == "Sonntag":
    print("Heute ist Wochenende, Zeit zum ausruhen.")


# if-else statement
today = "Mittwoch"
if today == "Samstag" or today == "Sonntag":
    print("Heute ist Wochenende, Zeit zum ausruhen.")
else:
    print("Die Arbeit ruft.")

# elif statement
today = "Sonntag"
if today == "Montag":
    print("Das Wochenende ist vorbei. 1. Arbeitstag")
elif today == "Sonntag" or today == "Samstag":
    print("Heute ist Wochenende, Zeit zum ausruhen.")
else:
    print("Die Arbeit ruft.")