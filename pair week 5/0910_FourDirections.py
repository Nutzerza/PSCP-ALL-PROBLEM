"""FourDirections"""
def print_up(counter):
    """print up"""
    if counter == 1:
        print("  *  ", end=" ")
    elif counter == 2:
        print(" *** ", end=" ")
    elif counter == 3:
        print("* * *", end=" ")
    elif counter == 4:
        print("  *  ", end=" ")
    elif counter == 5:
        print("  *  ", end=" ")

def print_down(counter):
    """print down"""
    if counter == 1:
        print("  *  ", end=" ")
    elif counter == 2:
        print("  *  ", end=" ")
    elif counter == 3:
        print("* * *", end=" ")
    elif counter == 4:
        print(" *** ", end=" ")
    elif counter == 5:
        print("  *  ", end=" ")

def print_left(counter):
    """print left"""
    if counter == 1:
        print("  *  ", end=" ")
    elif counter == 2:
        print(" *   ", end=" ")
    elif counter == 3:
        print("*****", end=" ")
    elif counter == 4:
        print(" *   ", end=" ")
    elif counter == 5:
        print("  *  ", end=" ")

def print_right(counter):
    """print right"""
    if counter == 1:
        print("  *  ", end=" ")
    elif counter == 2:
        print("   * ", end=" ")
    elif counter == 3:
        print("*****", end=" ")
    elif counter == 4:
        print("   * ", end=" ")
    elif counter == 5:
        print("  *  ", end=" ")

def main(txt):
    """print ans"""
    for counter in range(1, 6):
        for cha in txt:
            if cha == "U":
                print_up(counter)
            elif cha == "D":
                print_down(counter)
            elif cha == "L":
                print_left(counter)
            elif cha == "R":
                print_right(counter)
        print()
main(input())
