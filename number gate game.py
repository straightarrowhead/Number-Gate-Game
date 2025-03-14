import random

#initial values

levelCurrent = 1
hpPlayer = 10

# defines HP for boss's ranges per level
hpBossRanges = {

1: (50, 100),
2: (100, 150),
3: (150, 200),

}

print("Welcome to GateRunner! \n")
print("Your task is to collect enough willpower "
      "by going through gates and collecting more \n"
      "willpower. Will you have enough to defeat the boss at the end? \n")
print("\nYou begin with 10 willpower.")

def mainGame(gates):
    starterValue = 10
    for i in range(gates):
        print(f"You have {gates - i} gate(s) left.")
        setOfModifers = ["-10", "-20", "-30", "+10", "+20", "+30", "x2"]
        # setOfModifers = ["+10"]    
        setOfModifiers2 = ["/2", "/3", "/4", "+40", "+50", "+60", "x10"]
        # setOfModifiers2 = ["+40"]
        
        leftGate = random.choice(setOfModifers)
        rightGate = random.choice(setOfModifiers2)
        
        print("The left gate shows " + leftGate + ". "
        "Press a to go through the left gate.")
        
        print("The right gate shows " + rightGate + ". "
        "Press b to go through the right gate.")
        
        while True:
            choiceOfPlayer = input("Choose a gate--a or b: ").strip().lower()
            if choiceOfPlayer in ["a", "b"]:
                break
            print("Invalid choice. Please choose a or b")

        choiceOfGate = leftGate if choiceOfPlayer == "a" else rightGate


        if choiceOfGate == "-10":
            starterValue -= 10
        if choiceOfGate == "-20":
            starterValue -= 20
        if choiceOfGate == "-30":
            starterValue -= 30
        if choiceOfGate == "+10":
            starterValue += 10
        if choiceOfGate == "+20":
            starterValue += 20
        if choiceOfGate == "+30":
            starterValue += 30
        if choiceOfGate == "x2":
            starterValue *= 2
        if choiceOfGate == "/2":
            starterValue //= 2
        if choiceOfGate == "/3":
            starterValue //= 3
        if choiceOfGate == "/4":
            starterValue //= 4
        if choiceOfGate == "+40":
            starterValue += 40
        if choiceOfGate == "+50":
            starterValue += 50
        if choiceOfGate == "+60":
            starterValue += 60
        if choiceOfGate == "x10":
            starterValue *= 10

        print("\nYour current value is " + str(starterValue) + ".")

    return starterValue

while True:
    print(f"\n LEVEL {levelCurrent}")

    hpBossMin, hpBossMax = hpBossRanges.get(levelCurrent, (levelCurrent * 100, levelCurrent * 200))
    hpBoss = random.randint(hpBossMin, hpBossMax)

    print(f"The boss for level {levelCurrent} has {hpBoss} HP!")

    hpPlayer += mainGame(5)
    
    print(f"Your value after going through the gates is {hpPlayer}.")

    if hpPlayer >= hpBoss:
        print(f"You defeated the boss on level {levelCurrent}!")
        hpPlayer -= hpBoss
    else:
        print("Welp, you lost. Game over!")
        break #exit loop

    #prepares next level
    levelCurrent += 1

    continueRequest = input("You wanna go to the next level? y/n: ").lower()
    if continueRequest != "y":
        print("Game over! Thanks for playing.")
        break # exits loop
        
# print("This means...")

# if(hpPlayer <= hpBoss):
#     print("The boss beat you!")
# else:
#     print("You win!")
#     hpPlayer -= hpBoss
#     print("But, you took some damage. Your remaining willpower"
#           " after fighting the boss is " + str(hpPlayer) + ". \n")

print("More bosses coming later... >:)")
# print("And that time is now!")

# hpBoss = 10

# num2 = mainGame(3, 0)

# hpPlayer2 = hpPlayer + num2

# if(hpPlayer <= hpBoss):
#     print("The boss beat you this time!")
# else:
#     print("You won the game!")
#     hpPlayer -= hpBoss
#     print("Your remaining willpower is " + str(hpPlayer2) + ". \n")