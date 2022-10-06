"""Sequence XII"""
def main(num):
    """print ans"""
    count = num
    for row in range(num*2-1):
        for col in range(num*2-1):
            if row == col or col == num*2-2 - row:
                count = num
            print(str(count).zfill(2), end=" ")
            if (row < num) and ((col < num-1 and col >= row) or (col >= 2*num-2 - row and \
            col < num*2-2) or (col == num*2-2 and row != num-1)) or ((row >= num) and \
            (((col >= num*2-2 - row) and (col < num-1)) or \
            ((col >= row) and (col < num*2-2)))):
                count -= 1
            else:
                count += 1
        print()
main(int(input()))
