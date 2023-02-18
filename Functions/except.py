def main():
    try:
        num1=int(input('Enter a number:'))
        num2=int(input('Enter another number:'))
        result=num1 / num2
        print(num1, 'divided by ', num2, 'is', result)
    except:
        print('Error please enter a valid input or cant divid by 0')






main()
