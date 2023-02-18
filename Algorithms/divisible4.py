n=int(input('How many numbers are in the list?'))
list=[0]*n
print('Give me all the values of the list:')
for r in range(n):
    list[r]=int(input())
count=0
i=0
while i<n:
    if list[i] % 4 == 0:
        count+=1
    i+=1
if count>=n/2:
    print('at least have the element are divisible by 4')
else:
    print('less than half the list are divisible by 4 or none')
