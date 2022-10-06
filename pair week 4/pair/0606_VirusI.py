'''Virus'''
def main():
    '''eiei'''
    virus = input()
    total = 0
    for word in virus:
        if word == 'O':
            total += 0
        elif word == 'o':
            total += 1
    print(total)

main()
