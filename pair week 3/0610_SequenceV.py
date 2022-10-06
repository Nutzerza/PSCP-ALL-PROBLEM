"""Sequence V"""
def main(num):
    """loop for print ans"""
    counter = 1
    while True:
        if counter == 7:
            print(num, end="\n")
            counter = 1
        else:
            print(num, end=" ")
            counter += 1
        if num == 1:
            break
        num -= 1
main(int(input()))
