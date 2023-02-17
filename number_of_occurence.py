
def number_of_occurences(a,list1,size):
    count=0
    i=0
    while i < len(list1):
        if list1[i]==a:
            count+=1
        i+=1
    return count

def most_occuring(size, list1):
    most_occurrences=number_of_occurences(list1[0],list1,size)
    most_occuring=list1[0]
    i=2
    while i< len(list1):
        j=i+1
        count=1
        while j< len(list1):
            if list1[i]==list1[j]:
                count+=1
            j+=1
        if count>most_occurrences:
            most_occurrences=count
            most_occuring=list1[i]
        i+=1
    return most_occuring

def allEqual(size,list1):
    count=number_of_occurences(list1[0],list1,size)
    if count==len(list1):
        return True
    else:
        return False

def main():
    n=int(input('How many numbers are in the list?'))
    list_num=[0]*n
    print('Give me all the values of the list:')
    for r in range(n):
        list_num[r]=int(input())
    m_occuring=most_occuring(n, list_num)
    print('The most occuring number is:', m_occuring)
    equal=allEqual(n,list_num)
    print(equal)

main()
