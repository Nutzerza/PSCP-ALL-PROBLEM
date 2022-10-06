"""diamond"""
def main(num):
    """loop for print ans"""
    counter = 2
    for row in range(num):
        for col in range(num):
            if ((row <= num//2) and (col == num//2-row or row == num//2 or col == num//2+row)) \
            or ((row > num//2) and (col == row-num//2 or col == num-counter)):
                print("*", end="")
                if row > num//2 and col == num-counter:
                    counter += 1
            else:
                print(" ", end="")
        print()
main(int(input()))
