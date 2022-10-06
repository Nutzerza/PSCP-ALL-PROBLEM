"""RightArrow"""
def main(width, hight):
    """print ans"""
    for row in range(hight//2+1):
        for col in range(width+row):
            if col >= row:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    for row in range(hight//2-1, -1, -1):
        for col in range(width+row):
            if col >= row:
                print("*", end="")
            else:
                print(" ", end="")
        print()
main(int(input()), int(input()))
