"""Sequence XI"""
def print_top(num):
    """print top"""
    count = 1
    for row in range(1, num):
        for col in range(1, num*2):
            print(str(count).zfill(2), end=" ")
            if col <= num:
                if count != row:
                    count += 1
            else:
                if count == 1:
                    count += 0
                elif col <= num*2-row-1:
                    count += 0
                elif col > num:
                    count -= 1
        print()

def print_mid(num):
    """print mid"""
    count = 1
    for col in range(1, num*2):
        print(str(count).zfill(2), end=" ")
        if col < num:
            count += 1
        else:
            count -= 1
    print()

def print_bottom(num):
    """print bottom"""
    count = 1
    for row in range(num-1, 0, -1):
        for col in range(1, num*2):
            print(str(count).zfill(2), end=" ")
            if col <= num:
                if count != row:
                    count += 1
            else:
                if count == 1:
                    count += 0
                elif col <= num*2-row-1:
                    count += 0
                elif col > num:
                    count -= 1
        print()

def main(num):
    """cal func"""
    print_top(num)
    print_mid(num)
    print_bottom(num)
main(int(input()))
