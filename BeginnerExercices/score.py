#calculation of score but with try and except to prevent traceback if user enter wrong input 
score=input('Enter score:')
try:
    s=float(score)
except:
    print('Error please enter numeric number')
    quit()
if 0.0<s<1.0:
    if s>=0.9:
        print('A')
    elif s>=0.8:
        print('B')
    elif s>=0.7:
        print('C')
    elif s>=0.6:
        print('D')
    elif s<0.6:
        print('F')
else:
    print('Error number not in the range. Try again')
