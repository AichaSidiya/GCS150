def main():
    try:
        file1=input('filename:')
        new_list=write_file(file1)
        print(new_list)
        print('the number of lines in the file are:', len(new_list))
        num=int(input('How many lines do you want to display?'))
        display_line(num,new_list)
    except IOError:
        print('File dose not exist.')
    except ValueError:
        print('Number entered was not integer.')
    except IndexError:
        print('Index out of range')


def write_file(name):
    create_list=[]
    infile=open(name,'r')
    for word in infile:
        create_list+=[word.strip()]
    return create_list


def display_line(number, create_list):
    print(create_list[:number])

main()
