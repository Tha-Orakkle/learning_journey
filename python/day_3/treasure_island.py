#!/usr/bin/python3
import time
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

time.sleep(1)
print("Welcome to Treasure Island.")
time.sleep(2)
print("Your mission is to find the treasure in ...")
time.sleep(2)
print("3")
time.sleep(2)
print("2")
time.sleep(2)
print("1")
time.sleep(2)
print("YOUR JOURNEY BEGINS")
time.sleep(2)

ans = input("You're at a crossroad. Where do you want to go? " +
            "Type \"left\" or \"right\": ").lower()
if ans == "left":
    print("You've made a drastic turn into the realm of evil.")
    time.sleep(2)
    print("You find yourself in a valley, where the land has " +
          "long missed the bright smile of the sun but yet the stones " +
          "burn as hot as hell. The sandy trail, on each step, speaks to " +
          "your heels the number of lives it has stolen. You manage to " +
          "struggle your way out to the end of the valley. You are met " +
          "with a lake which covered a large aspect of your path. " +
          "On the left is tiny bridge. Where do you want to go?")
    ans = input("Swim or Bridge: ").lower()
    if ans == "bridge":
        time.sleep(1)
        print("You attempt to walk on the tiny bridge " +
              "you are met with an obstacle. Only the true in heart " +
              "and those found worthy shall trail this path.")
        time.sleep(1)
        print("To pass, solve this")
        time.sleep(1)
        ans = int(input("If two’s company and three’s a crowd " +
                        "what are four and five?.\nHint: it is a number: "))
        if ans == 9:
            time.sleep(1)
            print("You crossed the bridge and on the other side, you find " +
                  "a dark cave. In the grim darkness, afar was a " +
                  "glistering chest.")
            time.sleep(1)
            print("You found the chest")
            time.sleep(1)
            print("CONGRATULATIONS")
            time.sleep(1)
            print("YOU WON")
        else:
            time.sleep(1)
            print("If a you can not solve a simple riddle. You dont deserve " +
                  "a penny from the chest. You are blown by a strong " +
                  "into a pit woth spikes. The spikes grow longer and " +
                  "tear you apart.")
            time.sleep(1)
            print("GAME OVER")

    elif ans == "swim":
        time.sleep(1)
        print("As you dive into the almost freezing water. The lake " +
              "suddenly begins to create a path. It spreads open in half ")
        time.sleep(2)
        print("At first it appeared strange to you. but after walking a " +
              "you ease into it and keep walking. This must be " +
              "remembered as the day you made a wrong decision. " +
              "The water makes splashes of betrayal💦💦: it covers " +
              "you up and battles you like you are Percy Jackson ")
        time.sleep(2)
        print("You have drowned")
        time.sleep(2)
        print("GAME OVER")
    else:
        time.sleep(1)
        print("You've made a wrong decision. A strange worm appears🐛🐛" +
              " from nowhere and it swallows you up in whole")
        time.sleep(2)
        print("GAME OVER")
elif ans == "right":
    print("CONGRATULATIONS, YOU MANAGED TO FINSIH THE GAME BEFORE IT " +
          "EVEN STARTED. THE GRIM REAPER😈😈 HAS COME FOR YOU. YOUR " +
          "SOUL IS NO LONGER YOURS. ENJOY YOUR LAST 5 SECS")
    time.sleep(1)
    print("5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("GAME OVER")

else:
    time.sleep(1)
    print("You've made a wrong decision. You ate attacked by a bunch of " +
          "diabolic pirate and you soul is snatched...")
    time.sleep(2)
    print("GAME OVER")
