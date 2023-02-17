#calculating the gross pay but with calling a function you defined
def computpay(h,r):
    if h>40:
        a=h*r
        b=(h-40)*(r*0.5)
        p=a+b
        return p
    else:
        p=h*r
        return p
def main():
    hours=float(input('enter hours:'))
    rate=float(input('enter rate:'))
    p=computpay(hours,rate)
    print('Pay:', p)
main()
