#number=int(input('enter an integer number:'))
def sign(number):
    if number>0:
        print('Positive')
    elif number<0:
        print('Negative')
    else:
        print('Zero')
def even_odd(number):
    if number%2==0:
        print('Even')
    else:
        print('Odd')
def main():
    num=int(input('enter an integer number:'))
    sign(num)
    even_odd(num)

main()
