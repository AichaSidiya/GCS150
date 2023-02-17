#this program calculates the gross pay (p142)
BASE=40
OVERTIME_MULTIPLIER=1.5
#ask the user for the hour worked
hours=float(input('enter the number of extra hours'))
#ask the user for the hourly pay rate
rate=float(input('enter the rate:'))
if hours>BASE:
#find the overtime
	timeH=hours-BASE
#calculate the pay of overtime
	timeP=timeH*rate*OVERTIME_MULTIPLIER
#calculate the gross pay
	pay=base*rate+timeP
else:
	pay=hours*rate
#print the gross pay 
print('gross pay:',pay)
