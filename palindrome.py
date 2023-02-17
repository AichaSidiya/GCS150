n=int(input('The word is how many letters?'))
list=[0]*n
print('Give me the word you would like to check')
for r in range(n):
    list[r]=input()
palindrome = True
left = 0
right = n-1
while left<right and palindrome:
    if list[left]!= list[right]:
        palindrome = False
        print('This word is not a palindrome')
    else:
        left += 1
        right -= 1
if palindrome:
    print('This word is a palindrome')
