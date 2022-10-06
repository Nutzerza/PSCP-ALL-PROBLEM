"""Sequence XXX"""
def main(num_1, num_2):
    """print ans"""
    count = 0
    for row in range(num_1):
        for col in range(num_2*num_1+(num_2-1)):
            if count == num_1+1 or col == 0:
                count = 0
            if count == num_1:
                print(" ", end="")
            elif row == 0 or row == num_1-1 or count == row or count == num_1-1-row \
                or count == 0 or count == num_1-1:
                print("*", end="")
            else:
                print(" ", end="")
            count += 1
        print()
main(int(input()), int(input()))
