print("welcome to my quiz game :")

playing = input("Do you want to play th game? ").lower()

if playing != "yes":
    quit()
    
print("okey Lets play the game")

score = 0

# questions

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing ":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("you got " + str(score) + " qustions correct")
print("you got " + str((score)/4 * 100) + " %")