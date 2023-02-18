#range from 1->100.
#user should guess the number.
#if guess is greater than number than display(“Too high, try again.” ).
#if guess is less than number than display (“Too low, try again.” ).
#if he guess the number than print('congratulation').
#generate new number = loop.
#keep count of number of guess and display it.
import random
start_over=True
while start_over:
    number = random.randint(1, 101)
    guess= int(input('Enter number you believe is right or -1 to quit:'))
    count=1
    while guess != number and guess!=-1:
        if guess > number:
            print('Too high, try again')
        else:
            print('Too low, try again')
        guess = int(input('Enter number you believe is right:'))
        count+=1
    if guess!=-1:
        print('CONGRATULATION YOU GUESSED THE RIGHT NUMBER!!')
        print('You tried', count, 'times.')
    else:
        start_over=False
