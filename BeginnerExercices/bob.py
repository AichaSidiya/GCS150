#this program finds when the weight of laimark is greater than bob
#ask the user for the weight of laimark
x=int(input('weight laimark'))
#ask the user for the weight of bob
y=int(input('weight Bob'))
#initiate the years to 0
year=0
#a loop that finds the number of years
while x<=y:
    x=x*3
    y=y*2
    year=year+1
#printing the answer
print(year)
