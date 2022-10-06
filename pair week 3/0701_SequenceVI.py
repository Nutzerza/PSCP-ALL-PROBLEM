"""Sequence VI"""
def main(num):
    """loop for print ans"""
    for row in range(1, num+1):
        for col in range(row):
            print(col+1, end=" ")
        print()
main(int(input()))
