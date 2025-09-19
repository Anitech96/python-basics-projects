import random

easy_words= ["apple","train","tiger","money","india"]
medium_words= ["python","bottle","monkey","planet","laptop"]
hard_words= ["elephant","diamond","umbrella","computer","mountain"]

print("--WELCOME TO OUR WORD GUSSING GAME !--\n")
print("choose a difficulty level: Easy, Medium or Hard")

level= input("Enter the level :").lower()
if level == "easy":
    secret= random.choice(easy_words)
elif level == "medium":
    secret= random.choice(medium_words)
elif level == "hard":
    secret= random.choice(hard_words)
else:
    print("INVALID CHOICE 😖... \nDefaulting to easy level..")
    secret= random.choice(easy_words)

attempts=0
print("Guess the secreat word")

while True:
    guess= input("Enter your guess:").lower()
    attempts+=1

    if guess == secret:
        print(f'Congratulations! You gussed it in {attempts} attempts.')
        break
    
    hint= ""

    for i in range(len(secret)):
        if i<len(guess) and guess[i] == secret[i]:
            hint+= guess[i]
        else:
            hint+= "_"
    print("Hint:",hint)
print("GAME OVER ✨")
    