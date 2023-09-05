#Guessing Game
import random

score = 10
randomNumber = random.randint(1,10)

while True:
    userNumberInput = int(input('Guess: '))

    if userNumberInput == randomNumber:
        print('Congratulations you guessed it right, your score is ' + str(score))
        break
    else: 
        print('Better luck next time')
        score -= 1
    #Game Over
    if score <= 0:
        print('You lose, your score is ' + str(score))