# het spel van zoveel woorden met lengte 5  met  5 characters gokken in 1 minuut gokken.
# misschien beter als zoveel mogelijk woorden maken met de 5 charcters en niet
import random
import string

print('welkom bij het woorden spel')
print('u krijgt 5 letter waarbij u zoveel mogelijk woorden moet maken in 60 seconden')
print('wilt u het spel spelen?')
print('A.U.B. alleen met Ja of Nee antworden')

while True:
    antwoord = str(input())
    if antwoord == 'Ja':
        print('de game zal beginnen')
        False
    elif antwoord != 'Ja' or 'Nee':
        print('geen correcte invoer aub alleen Ja of Nee')
    elif antwoord == 'Nee':
        print('helaas dan niet')
        break
print('welkom bij het woorden spel, gok zoveel woorden met een lengte van 5')

randomletters = []

 #with open("sgb-words.txt", "r") as f:
  #  for line in f:
#        randomletters +=

klinkers = 'aeiuo'
medeklinkers = "bcdfghjklmnpqrstvwxyz"

letterlijst = []
# Willekeurige klinkers
for i in range(4):
     randomletter = random.choice(klinkers)
     letterlijst.append(randomletter)

# Willekeurige medeklinkers
for i in range(6):
    randomletter = random.choice(medeklinkers)
    letterlijst.append(randomletter)

letterlijst.sort()
print(letterlijst, end=' ')
print('')
# check als user wel echt maar 5 lang heeft
Guesswoord = str(input())
if len(str(Guesswoord)) == 14:
    True
else:
    print('woord kan alleen lengte 5 zijn, probeer nog eens')
#tijd afloop

BeginTijd = 60
while begintijd > 0:
    print(BeginTijd)
BeginTijd =  BeginTijd -1
if BeginTijd == 0:
    print('Je tijd is op')
else:
    print('je hebt nog tijd over')


