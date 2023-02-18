#This program determines whether a bank customer qualifies for a loan(p160)
MIN_SALARY=30000.0 #The minimum annual salary
MIN_YEARS=2 #The minimum years on the job
#Get the customer's annual salary.
salary=float(input('enter your annual salary:'))
#Get the number of years on the current job.
years_on_job=int(input('enter number of years employed:'))
#Determine whether the customer qualifies.
if salary>=MIN_SALARY or years_on_job>=MIN_YEARS:
#prints he is qualified
    print('you are qualified for the loan!')
else:
#print he is not qualified
    print('you are not qualified for the loan :(')
