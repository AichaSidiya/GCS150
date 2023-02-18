#try and except for gross pay 
hours=input('enter hours')
rate=input('enter rate')
try:
    h=float(hours)
    r=float(rate)
except:
    print('Error please enter numeric input')
quit()
if h>40:
    a=h*r
    b=(h-40)*(r*0.5)
    p=a+b
else:
    p=h*r
print(p)
