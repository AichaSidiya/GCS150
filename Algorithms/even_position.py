n=int(input('How many numbers are in the list?'))
list=[0]*n
print('Give me all the values of the list:')
for r in range(n):
    list[r]=int(input())
i = 0
while i < n:
    if i % 2 == 0:
        print('element', list[i], 'is in even position', i)
    i += 1
