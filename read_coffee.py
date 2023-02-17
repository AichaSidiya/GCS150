def coffee_read():
    found=False
    search=input('Enter a description to search for:')
    coffee_file=open('coffee.txt','r')
    descr=coffee_file.readline()
    while descr!='' or found==False:
        qty=float(coffee_file.readline())
        descr=descr.rstrip('\n')
        if descr==search:
            print('Description:', descr)
            print('Quantity:', qty)
            found=True
        descr=coffee_file.readline()
    coffee_file.close()
    if not found:
        print('That item was not found in the file.')

def main():
    print('Do you want coffee?')
    answer=input('answer:')
    while answer=='Y'or answer=='y':
        coffee_read()
        answer=input('answer:')
    print('Thank You, Bye')

main()
