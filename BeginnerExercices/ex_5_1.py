#count the number of elements in a given set, sum them and give the average.
count=0
total=0.0
#boolean loop
while True:
#ask the user for a set of numbers
    num=input('Enter a number:')
#ending input loop
    if num=='done':
        break
    else:
#making sure no traceback if user enters wrong input
        try:
            n=float(num)
        except:
            print('Invalid input. Please try again.')
            continue
    count=count+1
    total=total+n
#print the count, sum and average 
print('count:',count,'sum:',total,'average:',total/count)
