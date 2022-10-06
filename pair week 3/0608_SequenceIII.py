"""Sequence III"""
def main(num):
    """loop for print ans"""
    for row in range(1, num+1):
        for col in range(1, num+1):
            print(col+row, end=" ")
        print()
main(int(input()))
