# Guess my number 2
# The player has a limited chances to guess the number 

from random import randint 

secret_number = randint(1,100)

counter = 0
counter_limit = 6

n = int(input("Try a number: "))

if n < secret_number:
		print("Higher...")

elif n > secret_number:
		print("Lower...")

elif n == secret_number:
		print("Congratulations! You guessed the secret number!")
		print("The number of attempts was:",counter)
		
counter = counter + 1

while n != secret_number:

	n = int(input("Try again: "))

	counter = counter + 1


	if counter == counter_limit:
		print("Oh...I'm sorry.You used all your attempts :( ")
		break

	elif n < secret_number:
		print("Higher...")

	elif n > secret_number:
		print("Lower...")

	elif n == secret_number:
		print("Congratulations!The secret number was attempted in",counter,"times!")
