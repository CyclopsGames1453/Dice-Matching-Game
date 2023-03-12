import random
import numpy as np

# Enter number of players and players name
num_players = int(input("Enter the number of players: "))

playersName = np.empty((num_players), dtype='object')
playersScore = np.full((num_players), 0)

for i in range(0,num_players):
    playersName[i] = input("Enter player name: ")

dice = np.full((6), 0)
score = 0
gameEnd = False

# game

while True:
    for playerNumber in range(0,num_players):
        input("{} it's your turn. Press enter to roll the dice.".format(playersName[playerNumber]))
        remaining_dice = dice.size
        while True:

            # dice roll

            dice = np.full((remaining_dice), 0)

            turnScore = 0;

            for i in range(0,remaining_dice):
                dice[i] = random.randint(1, 6)
                print("You rolled : {}".format(dice[i]))

            # calculate possible combination

            combination = np.array([])

            for i in range(0,6):
                count = np.count_nonzero(dice == i)
                if count >= 3:
                    combination = np.append(combination, i)

            if combination.size < 1:
                print("Fail")
                print("{0} it's your score: {1}".format(playersName[playerNumber], playersScore[playerNumber]))
                break

            while True:
                # choose

                selection = input("Enter dice to keep (no spaces): ")
                selection_dice = 0

                # skip turn

                if selection == "":
                    playersScore[playerNumber] = score + playersScore[playerNumber]
                    print("{0} it's your score: {1}".format(playersName[playerNumber], playersScore[playerNumber]))
                    break

                # choose check

                selection_dice = dice[int(selection)-1]

                for i in range(0, remaining_dice):
                    if selection_dice in combination:
                        count = np.count_nonzero(dice == selection_dice)
                        if selection_dice == 1:
                            turnScore=1000
                            remaining_dice = remaining_dice - 3
                        else:
                            turnScore=selection_dice*100
                            remaining_dice = remaining_dice - 3

                        if selection_dice > 3:
                            turnScore = selection_dice * 2
                            remaining_dice = remaining_dice - 1
                        if selection_dice > 4:
                            turnScore = selection_dice * 2
                            remaining_dice = remaining_dice - 1
                        if selection_dice > 5:
                            turnScore = selection_dice * 2
                            remaining_dice = remaining_dice - 1

                        score = turnScore + score
                        if remaining_dice <= 0:
                            remaining_dice = 6
                        break

                if turnScore <= 0:
                    print("wrong choose")
                else:
                    selection = input("Do you continue (Y:Yes / N:No) : ")
                    break


            # game win

            if score+playersScore[playerNumber] > 5000:
                gameEnd = True
                print("!!! {0} Winner !!!".format(playersName[playerNumber]))
                break

            # skip turn

            if selection == "":
                break

            if selection == "N" or selection == "n":
                playersScore[playerNumber] = score + playersScore[playerNumber]
                print("{0} it's your score: {1}".format(playersName[playerNumber], playersScore[playerNumber]))
                break

        if gameEnd:
            break

    if gameEnd:
        break
