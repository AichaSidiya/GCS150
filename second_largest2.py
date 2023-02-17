n=int(input('How many numbers are in the list?'))
list=[0]*n
print('Give me all the values of the list:')
for r in range(n):
    list[r]=int(input())

if list[0]>list[1]:
    largest=list[0]
    second_largest=list[1]
else:
    largest=list[1]
    second_largest=list[0]
for i in range(3,n):
    if list[i]>largest:
        second_largest=largest
        largest=list[i]
    elif list[i]>second_largest:
        second_largest=list[i]

print('The largest number is:', largest,'The second largest is:', second_largest)
