print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("May the force be with you!")
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "control processing unit":
    print('Correct!')
    score +=1
else:
    print("Meh...Incorrect")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphic processing unit":
    print('Correct!')
    score +=1
else:
    print("Meh...Incorrect")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score +=1
else:
    print("Meh...Incorrect")

answer = input("What does PSU stand for? ")
if answer.lower() == "power suply unit":
    print('Correct!')
    score +=1
else:
    print("Meh...Incorrect")

print("You got " + str(score) + " questions correct!")
