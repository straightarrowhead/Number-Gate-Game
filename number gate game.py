import keyboard
import random

bossValue = 10
totalValue = 0
i = 10

print("Welcome to GateRunner! \n")
print("Your task is to collect enough willpower"
      "by going through gates and collecting more \n"
      "willpower. Will you have enough to defeat the boss at the end? \n")
print("\nYou begin with 10 willpower.")

def mainGame(i):
    n = 0
    starterValue = 10
    while i > 0:

        print("\nYou have " + str(i) + " gate(s) left.")
        setOfModifers = ["-10", "-20", "-30", "+10", "+20", "+30", "x2"]
        # setOfModifers = ["+10"]    
        setOfModifiers2 = ["/2", "/3", "/4", "+40", "+50", "+60", "x10"]
        # setOfModifiers2 = ["+40"]
        
        gateChoice = random.choice(setOfModifers)
        gateChoice2 = random.choice(setOfModifiers2)
        
        print("The left gate shows " + gateChoice + ". "
        "Press a to go through the left gate.")
        
        print("The right gate shows " + gateChoice2 + ". "
        "Press b to go through the right gate.")
        
        
        if keyboard.read_key() == "a":
            if gateChoice == "-10":
                starterValue -= 10
            if gateChoice == "-20":
                starterValue -= 20
            if gateChoice == "-30":
                starterValue -= 30
            if gateChoice == "+10":
                starterValue += 10
            if gateChoice == "+20":
                starterValue += 20
            if gateChoice == "+30":
                starterValue += 30
            if gateChoice == "x2":
                starterValue *= 2
                
        if keyboard.read_key() == "b":
            if gateChoice2 == "/2":
                starterValue //= 2
            if gateChoice2 == "/3":
                starterValue //= 3
            if gateChoice2 == "/4":
                starterValue //= 4
            if gateChoice2 == "+40":
                starterValue += 40
            if gateChoice2 == "+50":
                starterValue += 50
            if gateChoice2 == "+60":
                starterValue += 60
            if gateChoice2 == "x10":
                starterValue *= 10

        print("\nYour current value is " + str(starterValue) + ".")

        i -= 1
    n += starterValue
    print(n)
    return n

num = mainGame(5)

totalValue += num

print("Your value after going through the gates is " + str(totalValue) + ". \n")

# print("This means...")

# if(totalValue <= bossValue):
#     print("The boss beat you!")
# else:
#     print("You win!")
#     totalValue -= bossValue
#     print("But, you took some damage. Your remaining willpower"
#           " after fighting the boss is " + str(totalValue) + ". \n")

# print("More bosses coming later... >:)")
# print("And that time is now!")

# BossValue = 10

# num2 = mainGame(3, 0)

# totalValue2 = totalValue + num2

# if(totalValue <= bossValue):
#     print("The boss beat you this time!")
# else:
#     print("You won the game!")
#     totalValue -= bossValue
#     print("Your remaining willpower is " + str(totalValue2) + ". \n")