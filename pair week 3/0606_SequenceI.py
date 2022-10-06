"""Sequence I"""
def main(num):
    """loop for print ans"""
    for _ in range(1, num+1):
        for count in range(1, num+1):
            print(count, end=" ")
        print()
main(int(input()))
