# het spel van zoveel woorden met lengte 5  met  5 characters gokken in 1 minuut gokken.

import random
import string

print('welkom bij het woorden spel')
print('u krijgt 5 letter waarbij u zoveel mogelijk woorden moet maken in 60 seconden')
print('wilt u het spel spelen?')
print('A.U.B. alleen met Ja of Nee antworden')

antwoord = str(input())
if antwoord == 'Ja':
    print('de game zal beginnen')
elif antwoord != 'Ja' or 'Nee':
    print('geen correcte invoer aub alleen Ja of Nee')
elif antwoord == 'Nee':
    print('helaas dan niet')

# geef aantal letters tussen 3 tot 6
# laat tijd aflopen van 60 tot 1

print('welkom bij het woorden spel, gok zoveel woorden met een lengte van 5')

randomletters = []

 #with open("sgb-words.txt", "r") as f:
  #  for line in f:
#        randomletters +=

klinkers = 'aeiuo'
medeklinkers = "bcdfghjklmnpqrstvwxyz"

letterlijst = []
# Willekeurige klinkers
for i in range(2):
    randomletter = random.choice(klinkers)
    letterlijst.append(randomletter)

# Willekeurige medeklinkers
for i in range(3):
    randomletter = random.choice(medeklinkers)
    letterlijst.append(randomletter)

letterlijst.sort()
print(letterlijst, end=' ')
print('')
# check als user wel echt maar 5 lang heeft
Guesswoord = str(input())
if len(str(Guesswoord)) == 5:
    True
else:
    print('woord kan alleen lengte 5 zijn, probeer nog eens')
#tijd afloop




