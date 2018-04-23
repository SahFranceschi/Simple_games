#Guess my number 3
#The player thinks of a number and the computer has to guess it

from random import randint 

print("\nHey!! Think in a number between 1 and 100.\nI will try guess the number,ok?\n")

print("Write 'h' if your number is higher.")
print("Write 'l' if your number is lower.")
print("Write 'c' if the number is correct!")

input("\nPress ENTER to start!\n")

min = 1
max = 100
answer = ""

while answer != "c":

	n = randint(min,max)

	print("Is it",n,"?")
	answer = input("")

	if answer == "h":
		min = n + 1

	elif answer == "l":
		max = n - 1

	elif answer == "c":
		print("\nI GUESSED THE NUMBER!!! MUAHAHAHAHAH")

	else:
		print("Please enter a valid option.")


