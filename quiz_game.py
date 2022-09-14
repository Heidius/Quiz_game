print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Let's play :)")

answer = input("What does CPU stand for? ")
if answer == "control processing unit":
    print('Correct!')
else:
    print("Meh...Incorrect")

answer = input("What does GPU stand for? ")
if answer == "graphic processing unit":
    print('Correct!')
else:
    print("Meh...Incorrect")

answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print('Correct!')
else:
    print("Incorrect")

answer = input("What does PSU stand for? ")
if answer == "power suply unit":
    print('Correct!')
else:
    print("Incorrect")
