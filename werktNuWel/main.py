import random
import time

# ideeen
# nog met kleuren doen
# zorg ervoor dat letter niet 2 keer gegokt kan worden
# if gok == gebruikt:
  #  print("je hebt deze letter al gegokt, gok een andere letter")
# else:
  #  True
# make sure dat speler alleen met letters gokt print anders een foutmeldeing

def positie():

    print("welkom bij het woordgokspel, waarbij je het woord moet gokken")
    time.sleep(1)
    print("de naam maakt het totaal niet duidelijk waar de game ovver gaat ;)")
    time.sleep(1)
    print("het spel begint")
    time.sleep(1)

    with open('words.txt') as f:
        words = f.read().splitlines()
    f.close

    word = random.choice(words)
    word = word.lower()

    gebruikt = []

    display = word
    for i in range(len(display)):
        display = display[0:i] + "_" + display[i + 1:]

    print(" ".join(display))

    maxpogingen = len(word) + 2
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'

    while display != word:
        print("je hebt " + str(maxpogingen) + " pogingen")
        gok = input('gok een letter: ')
        gok = gok.lower()
        gebruikt.extend(gok)
        # print(pogingen)

        for i in range(len(word)):
            if word[i] == gok:
                display = display[0:i] + gok + display[i + 1:]
        print('gebruikte letters; ')
        print(gebruikt)

        print(" ".join(display))
        maxpogingen = maxpogingen - 1
        if maxpogingen == 0:
            print("helaas u heeft het woord niet gegokt")
            time.sleep(1)
            print("het correcte woord was" + str(word))
            time.sleep(1)
            break
    print("wilt u nog een spelen?")
    print("als je nog een keer wilt spelen antwoord met ja, j of nee, n ")


positie()

def welkomstscherm():

    while True:
        antwoord = input().lower()
        if antwoord in ["ja", "j"]:
            positie()
        elif antwoord in ["nee", "n"]:
            print("helaas veel plezier nog")
            break
        else:
            print("Dit is geen juist antwoord. Antwoord met j of n")


welkomstscherm()


""""
  while True:
  if gok != alphabet:
      print("u kunt alleen gokken met letters")
       continue
  elif gok in gebruikt:
      print("je hebt deze letter al gegokt, gok een andere letter")
      continue
  elif gok in word:
      print("deze letter zit in het woord")
      continue
  else;
      print("er ging iets mis")
      continue
  """
