#creating the list
rainfall=[]
for month in range(1,13):
    print('month', month, ':', end=' ')
    total_rainfall=int(input('Enter the total rainfall for this month:'))
    rainfall.append(total_rainfall)
#calculating the total rainfall of the year
total_year=0
for num in rainfall:
    total_year+=num
print('The total rainfall of the year is:',total_year) #printing the total rainfall of the year
#calculating average of the list
average= total_year/len(rainfall)
print('The average monthly rainfall is:', average)
#getting the maximum value and it's index
max_val= max(rainfall)
max_index=rainfall.index(max_val)
print('The highest month rainfall', max_index+1, 'The rainfall was', max_val)
#getting the minimum value and its index
min_val= min(rainfall)
min_index=rainfall.index(min_val)
print('The lowest month rainfall', min_index+1, 'The rainfall was', min_val)
