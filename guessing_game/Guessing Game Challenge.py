import random

print('Rules of the game: Guess between 1-10')

number = random.randint(1,10)

guesses = [1]


while True:

    guess = int(input('Please Guess between 1-10: '))

    if guess < 1 or guess > 10:
        print("Guess between 1-10")
        continue
        
    guesses.append(guess)

    if guess == number:
        print(f'Congrats it took you {len(guesses)} times!')
        break
    
    if guess < number:
        print('higher')
    else:
        print('lower')
          