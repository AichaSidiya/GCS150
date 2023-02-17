def remove_list(word_list):
    item=input('Enter the item that should I remove:')
try:
    list.remove(item)
    print('this is the list:')
    print(word_list)
except ValueError:
    print('the item was not found in the list')

main()
