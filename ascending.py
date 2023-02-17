n=int(input('How many numbers are in the list?'))
list=[0]*n
print('Give me all the values of the list:')
for r in range(n):
    list[r]=int(input())

ascending= True
i=0
while i<n and ascending:
    j=i+1
    while j<n and ascending:
        if list[j] < list[i]:
            ascending = False
            print('the list is not sorted in ascending order')
        else:
            j=j+1
    i=i+1
if ascending:
    print('the list is sorted in ascending order')
