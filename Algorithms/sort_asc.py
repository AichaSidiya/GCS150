def smallest_swap(list):
    i=0
    while i<len(list):
        j=i+1
        while j<len(list):
            if list[i] > list[j]:
                store=list[i]
                list[i]=list[j]
                list[j]=store
            j+=1
        i+=1
    return list



def sorting():
    n=int(input('How many numbers are in the list?'))
    new_list=[0]*n
    print('Give me all the values of the list:')
    for r in range(n):
        new_list[r]=int(input())
    sorted_list=smallest_swap(new_list)
    print(sorted_list)

sorting()
