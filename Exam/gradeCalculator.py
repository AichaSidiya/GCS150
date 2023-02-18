total_grade=0
for month in range(1,13):
    grade=int(input('What grade would you give us this month?'))
    if grade==10:
        print('Your customer gave you 10 in the month:', month)
    elif grade==1:
        print('Your customer gave you 1 in the month:', month)
    total_grade+=grade

average=total_grade/12
print('The average is:', average)
if average>=7:
    print('Customer satisfied!!!')
elif average>=5 and average<7:
    print('Customer is neutral')
else:
    print('Customer is not satisfied:(')
