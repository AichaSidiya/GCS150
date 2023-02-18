#find the largest and smallest number in a set
largest=None
smallest=None
while True:
    num=input('Enter a number:')
#to end the input and start the program.
    if num=='done':
        break
#revising the input ensuring it is an integer.
    try:
        n=int(num)
    except:
        print('Invalid input')
        continue
# the loop for finding the min an max in the set.
    if largest is None:
        largest=n
    elif n>largest:
        largest=n
    if smallest is None:
        smallest=n
    elif n<smallest:
        smallest=n
#print the answer.
print('Maximum is', largest)
print('Minimum is',smallest)
