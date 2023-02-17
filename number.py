#This program  generate a random number that the user have to guess, it contains multiple rounds.
def game(): #this function is the function that generates the random number and ask the user to guess it
	count=0 #counter that counts the number of tries before getting the right answer.
	import random
	number=random.randint(1,100) #variable that stores the random number generated.
	guess=int(input('Enter a number you guess is right')) #ask the useer to guess the number.
	while guess!=number: #loop that analysis the guess of the user.
		if guess>number:
			print('Too high, try again')
		else:
			print('Too low, try again')
		guess=int(input('Enter a number you guess is right')) #if the guess is less or greater than the number than the user have to guess again.
		count+=1 #update the count.
	if guess==number:
		print('Congratulation! your answer is correct', 'You tried', count+1, 'times') #when the user guess the right number he is congratulated by the program, and the program tell him the number of guess he made to find the answer.

def main(): #this function calls the game function and repeat it, if the user wants to play again.
    start=input('Fun game!Do you want to play?')
    while start=='yes':
        game()
        start=input('Fun game!Do you want to play again?')
    if start!='yes':
        print('bye')
main() #call main function.
