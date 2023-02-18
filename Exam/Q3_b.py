n=int(input('How many numbers are in the list?'))
list_num=[0]*n
print('Give me all the values of the list:')
for r in range(n):
    list_num[r]=int(input())
x=int(input('Enter a number to search for'))
def number_of_occurences(a,list1,size):
    count=0
    i=0
    while i < len(list1):
        if list1[i]==a:
            count+=1
        i+=1
    return count

occurence=number_of_occurences(x,list_num,n)
print('The number of occurences of',x, 'is:', occurence)
