# Guess my number 

from random import randint 

secret_number = randint(1,100)

counter = 1

n = int(input("Try a number: "))

if n < secret_number:
		print("Higher...")

elif n > secret_number:
		print("Lower...")

elif n == secret_number:
		print("Congratulations! You guessed the secret number!")
		print("The number of attempts was:",counter)
		
counter = counter + 1

while n != secret_number :

	n = int(input("Try a number: "))

	if n < secret_number:
		print("Higher...")

	elif n > secret_number:
		print("Lower...")

	elif n == secret_number:
		print("Congratulations! You guessed the secret number!")
		print("The number of attempts was:",counter)

	counter = counter + 1 
