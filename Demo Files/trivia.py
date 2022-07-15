score = 0
print("Welcome to trivia!")
print("You will be asked a series of questions. Answer as many as you can correctly!")
print("Good luck!")
print("")
print("1. What is the name of the famous plumber who was the main character in a series of games starting in the 1980s?")
print("a. John")
print("b. Paul")
print("c. George")
print("d. Mario")
print("")
answer = input("Press the letter of your answer: ")
if answer == "d":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("")
print("Final Score: ")
print(score)


