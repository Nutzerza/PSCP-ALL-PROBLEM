"""Stepper II"""
def main(num_1, num_2):
    """print ans"""
    if num_1 > num_2:
        for count in range(num_1, num_2-1, -1):
            print(count)
    else:
        for count in range(num_1, num_2+1, 1):
            print(count)
main(int(input()), int(input()))
