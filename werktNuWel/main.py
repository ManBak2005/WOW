import random

print("welcome to the word guessing game, where you have to guess the word")
print("wow the name does not make it absolutely obvious what it is about")
print("so are you down to play?")
print("if you want to play answer with Yes if you dont answer with No")

while True:
    answer = str(input())
    if answer == 'Yes':
        print('welcome to the word guess game')
        break
    elif answer == 'No':
        print("very unfortunate")
        break
    elif answer != 'Yes' or 'No':
        print('there was no correct input found, please only response with yes or no')

words = [words.txt]
# ff kijken hoe ik dat doe met de woorden uit de woordenlijst
word = random.choice(words)

lengt = [_]*len(word)

def PositionOfTheLetter:
