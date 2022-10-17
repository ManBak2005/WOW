import random

def PositionOfTheLetter(guess):
    if guess in word:
        index = word.find(guess)
     #pass


def WelkomstScherm():
    print("welcome to the word guessing game, where you have to guess the word")
    print("wow the name does not make it absolutely obvious what it is about")
    print("so are you down to play?")
    print("if you want to play answer with Yes if you dont answer with No")

#def stelJaNeeVraag(vraag):
    while True:
        antwoord = input().lower()
        if antwoord in ["ja","j"]:
            return "ja"
        elif antwoord in ["nee", "n"]:
            return "nee"
        else:
            print("Dit is geen juist antwoord. Antwoord met j of n")

"""
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
"""

# Zet wat spullen voor het spel klaar

# bestand lezen en de inhoud in een lijst plaatsen
with open('words.txt') as f:
    words = f.read().splitlines()
f.close
for i in range (1):
    print(i)
spelActief = True

WelkomstScherm()

while spelActief:
    # dit is de grote spel-lus

    # kies een willekeurig woord

    word = random.choice(words)
    print(word)
    # bepaal maximaal aantal pogingen
    maxpoging = len(word)+2
    score = 0

    # druk de lege string met streepjes af

    raadlijst = len(word)*["_"]
    print(raadlijst)




    # einde van het spel
#    antwoord = stelJaNeeVraag("Wilt u nog een keer spelen?")
#    if antwoord == "nee":
#        spelActief = False

    # einde grote spel-lus.

# ff kijken hoe ik dat doe met de woorden uit de woordenlijst
#word = random.choice(words)

#print(f"+++ {word}")
#lengt = ["_"]*len(word)

