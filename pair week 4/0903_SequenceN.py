"""Sequence N"""
def main(num):
    """print ans"""
    for row in range(num):
        for col in range(num):
            if row == col or col == 0 or col == num - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
main(int(input()))
