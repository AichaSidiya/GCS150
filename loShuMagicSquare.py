def main():
    two_dim=two_dim_list()
    print(two_dim)
    Lo_Shu(two_dim)
def two_dim_list():
    import random
    two_list=[[0]*3]*3
    for r in range(3):
        for c in range(3):
            two_list[r][c]= random.randrange(1,10)
    return two_list

def Lo_Shu(two_list):
    if two_list[0][0]+two_list[1][0]+two_list[2][0]==two_list[0][0]+two_list[0][1]+two_list[0][2]==two_list[0][0]+two_list[1][1]+two_list[2][2]:
        print('The list is a Lo Shu Magic Square.')
    else:
        print('The list is not a Lo Shu Magic Square.')

main()
 
