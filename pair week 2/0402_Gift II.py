"""Gift II"""
def check_even(num_1, num_2):
    """check even"""
    if num_1%2 == 0:
        return num_1
    elif num_2%2 == 0:
        return num_2
    else:
        return 0
def main(even_gift=0):
    """print ans"""
    even_gift += check_even(int(input()), int(input()))
    even_gift += check_even(int(input()), int(input()))
    even_gift += check_even(int(input()), int(input()))
    even_gift += check_even(int(input()), int(input()))
    print(even_gift)
main()
