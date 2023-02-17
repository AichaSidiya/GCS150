def nb_bits(number):
    nums=str(number)
    list1=[]
    for n in nums:
        list1+=[int(n)]
    bit=0
    for num in list1:
        bit+=1
    print('This number is', bit, 'bit')
    return list1

def give_value(bit, position):
    return bit*2**position

def convert(binary_number):
    list_bit=nb_bits(binary_number)
    decimal=0
    i=0
    pos=len(list_bit)-1
    while i< len(list_bit):
        decimal+=give_value(list_bit[i],pos)
        i+=1
        pos-=1
    return decimal

def main():
    number=int(input('Enter the binary number you want to convert'))
    conversion=convert(number)
    print('The decimal equvilant is:', conversion)

main()
