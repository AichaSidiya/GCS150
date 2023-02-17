n=int(input('How many numbers are in the list?'))
list=[0]*n
print('Give me all the values of the list:')
for r in range(n):
    list[r]=int(input())
count = 0
i = 0
while i<n:
    if list[i] == 0:
        count += 1
    i += 1
print('0 occured', count, 'times in this list')
