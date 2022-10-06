"""Parallelogram"""
def main(txt):
    """print ans"""
    for row in range(1, len(txt)+1):
        for col in range(len(txt)):
            if col == len(txt)-row:
                print(txt[:row], end="")
            else:
                print(" ", end="")
        print()

    for row in range(1, len(txt)):
        for col in range(len(txt)):
            if col == 0:
                print(txt[row:], end="")
            else:
                print(" ", end="")
        print()
main(input())
