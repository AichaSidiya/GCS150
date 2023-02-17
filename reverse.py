n=int(input('How many numbers are in the list?'))
list=[0]*n
print('Give me all the values of the list:')
for r in range(n):
    list[r]=int(input())
left = 0
right = n-1
sotre=0
while left<right:
    store = list[left]
    list[left] = list[right]
    list[right] = store
    left += 1
    right -= 1
print('The new reversed list is:', list)
