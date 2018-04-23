##################################
#             IMPORTS            #
##################################

from random import randint 

##################################
#             CONSTANTS          #
##################################

INITIAL_CREDITS = 600

##################################
#             variables          #
##################################

credits = INITIAL_CREDITS

score = {15:50, 16:100, 17:200, 18:250, 19:300, 20:400}

print("\n\n")

print("                             ##############")
print("                             #   QUASAR   #")
print("                             ##############\n\n")


print("* Pay 200 credits to play ONE round.")
print("* The objective is make 20 points or close to 20 points.")
print("* You will receive some credits according to your score.\n")

print("      --------------------------")
print("     |   Points   |   credits   |")
print("     |--------------------------|")
print("     |     20     |     400     |")
print("     |     19     |     300     |")
print("     |     18     |     250     |")
print("     |     17     |     200     |")
print("     |     16     |     100     |")
print("     |     15     |     050     |")
print("      --------------------------")

    
print("\nYou are in a Cassino and see a Quasar. You put your hand in your pocket and find",credits,"credits.")
answer = input("Do you want to play a round of Quasar? ( y / n ) ")


while answer != "n":

    if credits >= 200: 

        points = randint(1,5)

        credits -= 200

        while points < 15:

            print("\n\nNow you have",points,"points.\n")

            print("Choose one of the options below:\n")

            print("a)Take a number between 4 and 7.")
            print("b)Take a number between 1 and 8.")

            option = input("\nI will take the option: ")

            if option == "a": 

                points += randint(4,7)

            elif option == "b":

                points += randint(1,8)

            else:

                print("\nPlease, enter a valid option.\n")

        while points <= 20:


            print("\nNow you have",points,"points.\n")

            print("Choose one of the options below:\n")

            print("a)Take a number between 4 and 7.")
            print("b)Take a number between 1 and 8.")
            print("c)Leave with",points,"points and receive the credits.")

            option = input("\nI will take the option: ")

            if option == "a": 

                points += randint(4,7)

            elif option == "b":

                points += randint(1,8)

            elif option == "c":

                print("\n\nYou make",points,"points and receive",score.get(points),"credits.\n\n")

                credits += score.get(points)

                break

            else:

                print("\nPlease, enter a valid option.\n")

        else:

            print("\nI'm sorry! Your score is bigger then 20 points. You loose :(\n")


    print("\n\nYou have",credits,"credits.")
    answer = input("Do you want to play again? ( y / n ) ")

    if answer == "n":

        print("\nBye bye...\n\n")
