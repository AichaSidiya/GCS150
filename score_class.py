#this program tell u your grade letter based on your score
A=90
B=80
C=70
D=60
#ask the user for their grade
score=int(input('enter score'))
#condition that determine your grade 
if score>=A:
    print('your grade is A')
elif score>=B:
    print('your grade is B')
elif score>=C:
    print('your grade is C')
elif score>=D:
    print('your grade is D')
else:
    print('your grade is F')
