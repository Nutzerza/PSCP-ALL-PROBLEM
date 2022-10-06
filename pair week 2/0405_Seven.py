"""Seven"""
def check_num(num):
    """check and return"""
    if num == 1:
        return 7
    elif num == 2:
        return 9
    elif num == 3:
        return 3
    elif num == 0:
        return 1

def main(num):
    """print ans"""
    print(check_num(num%4))
main(int(input()))
