def string(number):
    nums=str(number)
    return nums

def list_creator(nums):
    list1=[]
    for num in nums:
        list1+=[int(num)]
    return list1

def total(list1):
    total=0
    for n in list1:
        total+=n
    return total

def main():
    num=int(input('enter a number:'))
    str_num=string(num)
    new_list=list_creator(str_num)
    tot=total(new_list)
    while tot>=10:
        str_num=string(tot)
        new_list=list_creator(str_num)
        tot=total(new_list)
    if tot==3 or tot==6 or tot==9:
        print('Number is divisble by 3.')
    else:
        print('Number not divisible by 3.')

main()
