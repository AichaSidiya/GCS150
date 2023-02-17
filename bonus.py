def repeat(string,number):
    new_string=''
    for i in range(number):
        new_string+=string
    print(new_string)

def main():
    s=input('enter a word:')
    num=int(input('enter a number: '))
    repeat(s,num)

main()
