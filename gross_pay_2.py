#this program calcylates the grass pay
hours=input('enter hours') #asking user for the number of hours
h=float(hours) #changing the input to float to be able to calculate
rate=input('enter rate') #asking the user for the hourly pay rate
r=float(rate) #changing the input to float to be able to calculate
#condition to calculate the gross pay
if h>40:
    a=h*r
    b=(h-40)*(r*0.5)
    p=a+b
else:
    p=h*r
#printing the answer 
print(p)
