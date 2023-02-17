def main():
    golf_file=open('golf.txt','r')
    name=golf_file.readline()
    while name!='':
        score=golf_file.readline()
        name=name.rstrip('\n')
        score=score.rstrip('\n')
        print('Name:', name)
        print('Score:', score)
        print()
        name=golf_file.readline()
    golf_file.close()

main()
