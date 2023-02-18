n=int(input('How many numbers are in the list?'))
list_num=[0]*n
print('Give me all the values of the list:')
for r in range(n):
    list_num[r]=int(input())
ones_complement=[]
for num in list_num:
    if num==0:
        num=1
    else:
        num=0
    ones_complement+=[num]

print('This is the ones complement of the number:', ones_complement)
