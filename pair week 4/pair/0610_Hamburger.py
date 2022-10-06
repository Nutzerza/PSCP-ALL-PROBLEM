'''hamburger'''
def main():
    '''eiei'''
    front_bread = int(input())
    back_bread = int(input())
    meat = (front_bread + back_bread)*2
    print('|'*front_bread + '*'*meat + '|'*back_bread)
main()
