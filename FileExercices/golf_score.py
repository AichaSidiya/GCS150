def main():
    num_players=int(input('How many players are in the team?'))
    golf_file=open('golf.txt', 'w')
    for count in range(1, num_players+1):
        print('Enter data for players #', count, sep='')
        name=input('name:')
        score=input('score:')
        golf_file.write(name + '\n')
        golf_file.write(score+ '\n')
    golf_file.close()
    print('Players records written to golf.txt')

main()
