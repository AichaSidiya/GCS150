def main():
    k=float(input('enter distance in kilometer:'))
    print('the number of miles is:', convert(k))

def convert(kilometer):
    miles=kilometer*0.6214
    return miles

main()
#return: youbare going to use it again in the program.
