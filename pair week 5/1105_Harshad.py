"""Harshad"""
def find_digit(num):
    """sum digit"""
    total = 0
    if int(num) < 0:
        counter = 1
    else:
        counter = 0
    for _ in range(len(num)-counter):
        total += int(num[counter])
        counter += 1
    return total

def main():
    """print ans"""
    for _ in range(10):
        num = input()
        digit = find_digit(num)
        if digit == 0:
            print("No")
        elif int(num) % digit != 0:
            print("No")
        else:
            print("Yes")
main()
