import random

print("wELCOME TO WIZARD BATTLE")
gameselect = input("Would you like to play single-player mode or multiplayer mode? (s or m)").lower()

if gameselect == "m":
   player1name = input("What is your name young wizard? ").capitalize()
   player2name = input("What is your name young wizard? ").capitalize()
   print("ThiS Wizard Battle will be between", player1name, "and", player2name,". Prepare to cast your spells!")

   player1lives = 3
   player2lives = 3

   options = ["Fire", "Water", "Ice"]
   player1pick = None
   player2pick = None

   while player1lives and player2lives != 0:
       player1pick = input("Alright,",player1name,"cast your spell: Water, Fire, or Ice! ")
       player2pick = input("Alright,",player2name,"cast your spell: Water, Fire, or Ice! ")

        if player1pick == "":
            print(player1name, "did not cast a spell")
        elif player2pick == "":
            print(player2name, "did not cast a spell")
        
        else:
            print(player1name,"casted", player1pick)
            print(player2name,"casted", player2pick)

        if player1pick == player2pick:
            print("The spells cancelled eachother out, recast your spell!")
        elif player1pick == "":
            print("You took a direct hit,", player1name, "use a spell next time!")
            player1lives -1
        elif player2pick == "":
            print("You took a direct hit,", player2name, "use a spell next time!")
            player2lives -1
        elif player1pick == "Fire":
            if player2pick == "Ice":
                print("You're spell overpowered", player2name, "you have done damage!")
                player2lives -1
            elif player2pick == "Water":
                print("You're spell was overpowered by", player2name, "you have taken damage!")
                player1lives -1
        elif player1pick == "Water":
            if player2pick == "Fire":
                print("You're spell overpowered", player2name, "you have done damage!")
                player2lives -1
            elif player2pick == "Ice":
                print("You're spell was overpowered by", player2name, "you have taken damage!")
                player1lives -1
        elif player1pick == "Ice":
            if player2pick == "Water":
                print("You're spell overpowered", player2name, "you have done damage!")
                player2lives -1
            elif player2pick == "Fire":
                print("You're spell was overpowered by", player2name, "you have taken damage!")
                player1lives -1

elif gameselect == "s":
    playername = input("What is your name young wizard? ").capitalize()
    wizards = ["Scrappy Spellmore","Twinkle Starwind","Chad Thundercast","Jafar Talithone","Lord Couldron"]
    wizardname = random.choice(wizards)

    CPUlives = 3
    playerlives = 3

    playermoney = 0

    while True:
        options = ["Fire", "Water", "Ice"]
        CPUpick = random.choice(options)
        playerpick = None

        print("Welcome", playername, "your first opponent will be", wizardname)
        playerpick = input("Cast your spell: Fire, Water, or Ice! ").capitalize()

        if playerpick == "":
            print(playername, "did not cast a spell")
        else:
            print(playername,"casted", playerpick)
        print(wizardname,"casted", CPUpick)

        if playerpick == CPUpick:
            print("The spells cancelled eachother out, recast your spell!")
        elif playerpick == "":
            print("You took a direct hit,", playername, "use a spell next time!")
        elif playerpick == "Fire":
            if CPUpick == "Ice":
                print("You're spell overpowered", wizardname, "you have done damage!")
            elif CPUpick == "Water":
                print("You're spell was overpowered by", wizardname, "you have taken damage!")
        elif playerpick == "Water":
            if CPUpick == "Fire":
                print("You're spell overpowered", wizardname, "you have done damage!")
            elif CPUpick == "Ice":
                print("You're spell was overpowered by", wizardname, "you have taken damage!")
        elif playerpick == "Ice":
            if CPUpick == "Water":
                print("You're spell overpowered", wizardname, "you have done damage!")
            elif CPUpick == "Fire":
                print("You're spell was overpowered by", wizardname, "you have taken damage!")
    
        playagain = input("Would You like to battle again? (y/n) ").lower()
        if playagain != "y":
            break