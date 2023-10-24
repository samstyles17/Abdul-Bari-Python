import random
n = random.randint(1,10)

guess = 0

while guess != n:
    guess = int(input('Enter your guess:'))
    if guess < n:
        print('Guess less than value')
    elif guess > n:
        print('Guess greater than the number')
    else:
        print("Correct!")