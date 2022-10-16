import random
import time
import pygame



print('welkom bij het woorden spel')
print('u krijgt 5 letter waarbij u zoveel mogelijk woorden moet maken in 60 seconden')
print('wilt u het spel spelen?')
print('A.U.B. alleen met Ja of Nee antworden')

while True:
    antwoord = str(input())
    if antwoord == 'Ja':
        print('de game zal beginnen')
        print('welkom bij het woorden spel, gok zoveel woorden met een lengte van 5')
        break
    elif antwoord != 'Ja' or 'Nee':
        print('geen correcte invoer aub alleen Ja of Nee')
    elif antwoord == 'Nee':
        print('helaas dan niet')
        break

randomletters = []

klinkers = 'aeiuo'
medeklinkers = "bcdfghjklmnpqrstvwxyz"

letterlijst = []

for i in range(2):
     randomletter = random.choice(klinkers)
     letterlijst.append(randomletter)


for i in range(3):
    randomletter = random.choice(medeklinkers)
    letterlijst.append(randomletter)

 with open("alle woorden.txt", "r") as f:
    for line in f:
        print(line)

# while loop maken zodat timer niet gelijk afgaat?

BeginTijd = 59

for i in range(BeginTijd):
    print(BeginTijd-i)
    time.sleep(1)
print('Je tijd is op')

letterlijst.sort()
print(letterlijst, end=' ')
print('')

Guesswoord = str(input())

if len(str(Guesswoord)) == 5:
    True
else:
    print('woord kan alleen lengte 5 zijn, probeer nog eens')

# with open("sgb-words.txt", "r") as f:
  #  for line in f:
#        randomletters +=


