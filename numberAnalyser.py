def number_analyser():
    n_list=number_list()
    print(n_list)
    smallest=lowest(n_list)
    print('The lowest value in the list is:',smallest)
    largest=highest(n_list)
    print('The lowest value in the list is:',largest)
    av=average(n_list)

def number_list():
    number_list=[]
    for n in range(20):
        number=int(input('what number you want to add to the list?'))
        number_list+=[number]
    return number_list

def lowest(number_list):
    smallest_number_so_far=number_list[0]
    i=1
    while i<len(number_list):
        if number_list[i]<smallest_number_so_far:
            smallest_number_so_far=number_list[i]
        i+=1
    return smallest_number_so_far

def highest(number_list):
    largest_number_so_far=number_list[0]
    i=1
    while i<len(number_list):
        if number_list[i]>largest_number_so_far:
            largest_number_so_far=number_list[i]
        i+=1
    return largest_number_so_far

def average(number_list):
    total=0
    for num in number_list:
        total+=num

    avg=total/len(number_list)
    print('The average of the list is:',avg)
    return avg

number_analyser()
 
