# Game name: Treasure Runner
# You are building a menu game where the player tries to reach 20 coins before they run out of HP.
# Starting values
# HP starts at 10
# Coins start at 0
# Potions start at 1
# HP max is 10
#
# Menu options (must be exactly these)
# Explore
# Rest
# Use potion
# Shop
# Status
# Quit
#
# Rules
# 1) Explore
# Random event:
# 60%: gain 1 to 5 coins
# 30%: lose 1 to 4 HP
# 10%: jackpot gain 5 to 10 coins

# 2) Rest
# Heal 1 to 3 HP, but HP cannot exceed 10.

# 3) Use potion
# If potions > 0: potions -1, HP +5 (max 10)
# If no potions: show message

# 4) Shop
# Potion costs 6 coins
# Ask: Buy potion? (y/n)
# Validate y/n
# If enough coins, coins -6, potions +1

# 5) Status
# Print: HP, Coins, Potions

# 6) Quit
# Exit game
# Validation requirements (must do)
# Menu input must be a number
# Menu number must be between 1 and 6
# Shop input must be only y or n
# Use continue to re-ask on invalid inputs
# Win and lose conditions
# If coins >= 20: player wins
# If HP <= 0: game over

# Win and lose conditions
# If coins >= 20: player wins
# If HP <= 0: game over
#
# Slightly harder add-on challenge (optional)
# Add option 7) Gamble
# Costs 3 coins to play (must have at least 3)
# 50% win: +6 coins
# 50% lose: -2 HP


hp = 10
coins = 0
potions = 1

import random

print("Welcome to Treasure Runner!")
print("Goal: Get 20 coins before your HP hits 0.")
Dailybonus = random.randint (1,10)

if Dailybonus == (1 or 2):
    print("You got 5 free coins!")
    coins = coins + 5

elif Dailybonus == 3:
    print("You got 1 free potion!")
    potions = potions + 1

else:
    print("You did not get anything from the Daily Bonus Lucky Draw!")

while True:

    print("꧁𓊈𒆜 MENU 𒆜𓊉꧂")
    print("1. Explore🧭️")
    print("2. Rest🛌")
    print("3. Use Potions🧪")
    print("4. Shop🛒")
    print("5. Status📊")
    print("6. Quit🔚")
    print("7. Gamble🎰")
    try:
        answer = int(input("Enter your choice:"))
    except ValueError:
        print("Please enter 1, 2, 3, 4, 5, 6 or 7.")
        continue

    if answer == 1:
        chances = random.randint(1, 10)

        if chances == 1:
            coinsmb = random.randint(5, 10)
            coins = coins + coinsmb
            print("Jackpot! You got", coinsmb, "more coins from the jackpot! Now you have", coins, "coins.")
            if coins >= 20:
                print("You Win!")
                break

        elif chances in (2, 3, 4):
            injured = random.randint(1, 4)
            hp -= injured

            if hp <= 0:
                print("Game Over!")
                break
            else:
                print("You got hurt by an enemy! You have", hp, "HP left.")

        else:
            chances1 = random.randint(1, 5)
            coins = coins + chances1
            print("You got", chances1, "coins from your adventure!")
            if coins >= 20:
                print("You Win!")
                break

    elif answer == 2:
        if hp == 10:
            print("You already have full health (10 HP).")
        else:
            rested = random.randint(1, 3)
            hp = hp + rested
            if hp > 10:
                hp = 10
            print("You now have", hp, "health points.")

    elif answer == 3:
        if potions >= 1:
            potions = potions - 1
            hp = hp + 5
            if hp > 10:
                hp = 10
            print("You used a potion and gained 5 health points! Now you have", potions, "potions and", hp, "health points.")
        else:
            print("You do not have potions. You can buy potions in the shop.")

    elif answer == 4:
        pots = input("Do you want to buy a potion for 6 coins? y/n:").lower()
        if pots == 'y':
            if coins >= 6:
                potions = potions + 1
                coins = coins - 6
                print("You now have", potions, "potions left.")
            else:
                print("You do not have enough coins. See you next time!")
        elif pots == 'n':
            print("You may come back next time! See you!")
        else:
            print("Please enter y/Y or n/N.")

    elif answer == 5:
        print("You have", hp, "health points, ", coins, "coins, and", potions, "potions.")

    elif answer == 6:
        print ("Thanks for playing!")
        break

    elif answer ==  7:
        gamble = input("Do you want to play a gamble? y/n:").lower()
        if gamble == 'y':
            if coins >= 3:
                g = random.randint(1, 10)
                if g in [1,2,3,4,5]:
                    hp = hp - 2
                    print("You have lost the gamble and lost 2 health points. Now you have", hp, "health points.")
                    if hp <= 0:
                        print("Game Over!")
                        break
                else:
                    coins = coins + 6
                    print("You have earned 6 coins. Now you have", coins, "coins.")
                    if coins >= 20:
                        print("You Win!")
                        break
            else:
                print("You do not have enough coins. See you next time!")
        elif gamble == 'n':
            print("See you next time here to gamble!")
        else:
            print("Please enter y/Y or n/N.")

    else:
        print("Invalid answer. Please enter 1, 2, 3, 4, 5, or 6.")