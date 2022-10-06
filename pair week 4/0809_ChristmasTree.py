"""ChristmasTree"""
def print_leaf(num_top):
    """print leaf"""
    for row in range(1, num_top+1):
        for col in range(1, num_top*2):
            if col > num_top - row and col < num_top + row:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_trunk(num_top, num_bottom):
    """print trunk"""
    for _ in range(num_bottom):
        print(" "*(num_top-2) + "-"*3)

def main(num_top, num_bottom):
    """call func"""
    print_leaf(num_top)
    print_trunk(num_top, num_bottom)
main(int(input()), int(input()))
