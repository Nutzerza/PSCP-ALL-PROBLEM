"""Sequence IX"""
def main(num):
    """loop for print ans"""
    count = num-1
    for row in range(1, num+1):
        counter = 0
        for col in range(num*2-1):
            if col >= num - row and col < (num*2-1)-count:
                print(str(counter+1).zfill(2), end=" ")
                if col >= num-1:
                    counter -= 1
                else:
                    counter += 1
            else:
                print("  ", end=" ")
        count -= 1
        print()
main(int(input()))
