#The program display the number of calories burned after 10, 15, 20, 25, and 30 minutes.
calories_burned_per_minute=float(input('enter calories burned per-minute')) #ask the user about the number of calories burned per minute.
while calories_burned_per_minute<4 or calories_burned_per_minute>7:
    print('error the calories-burned should not be less then 4')
    print('error the calories-burned should not be greater then 7')
    calories_burned_per_minute=float(input('enter calories burned per-minute')) #ask the user about the number of calories burned per minute
#this loop will calculate the number of calories burned for the time of the workout
for time in range(10,35,5):
    calories_burned=calories_burned_per_minute*time
    print('You workout for:',time,'minute and you burned',calories_burned, 'calories')
