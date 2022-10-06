"""Sequence X"""

def print_on_top(num):
    """print on top"""
    count = num-1
    for row in range(1, num+1):
        counter = 1
        for col in range(num*2-1):
            if col >= num - row and col < (num*2-1)-count:
                print(str(counter).zfill(2), end=" ")
                if col >= num-1:
                    counter -= 1
                else:
                    counter += 1
            else:
                print("  ", end=" ")
        count -= 1
        print()

def print_bottom(num):
    """print bottom"""
    for row in range(1, num):
        counter = 1
        for col in range(num*2-1):
            if col >= row and col < (num*2-1) - row:
                print(str(counter).zfill(2), end=" ")
                if col >= num-1:
                    counter -= 1
                else:
                    counter += 1
            else:
                print("  ", end=" ")
        print()

def main(num):
    """call function to print"""
    print_on_top(num)
    print_bottom(num)

main(int(input()))
