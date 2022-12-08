import random
import time
import cv2


def positie():

    print("Welkom bij het woordgokspel, gok een woord van lengte 5.")
    time.sleep(1)
    print("Als je de correcte letter gokt komt het in de juiste positie.")
    time.sleep(1)
    print("U heeft 10 pogingen, het spel begint.")
    time.sleep(1)

    with open('sgb-words.txt') as f:
        words = f.read().splitlines()

    word = random.choice(words)

    gebruikt = []

    display = word
    for i in range(len(display)):
        display = display[0:i] + "_" + display[i + 1:]

    print(" ".join(display))

    maxpogingen = len(word) + 5
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'

    while display != word:
        print("je hebt " + str(maxpogingen) + " pogingen")
        gok = input('gok een letter: ')

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
            print("het correcte woord was: " + str(word))
            print('aub sluit de foto')
            time.sleep(1)
            img_b = cv2.imread('thi_baby.jpg')
            cv2.imshow('image' ,img_b)
            cv2.waitKey(10)
            break
        elif word == display:
            print("u heeft het woord correct geraden")
            print("daarom kunt ie deze mooie foto bewonderen")
            time.sleep(1)
            img_a = cv2.imread('sussy.jpg')
            cv2.imshow('image' ,img_a)
            cv2.waitKey(1000)
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