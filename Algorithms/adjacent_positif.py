n=int(input('How many numbers are in the list?'))
list=[0]*n
print('Give me all the values of the list:')
for r in range(n):
    list[r]=int(input())
found=False
i=0
j=i+1
while i<n and j<n and not found:
    if list[i]>=0 and list[j]>=0:
        found=True
        print('there is tow positive adjacent numbers'+ 'and they are:', list[i], 'and', list[j])
    else:
        i+=1
        j+=1
if not found:
    print('there is no positive adjacent numbers')
