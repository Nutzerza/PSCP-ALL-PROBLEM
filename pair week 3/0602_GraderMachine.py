"""GraderMachine"""
def main(start, end):
    """print ans"""
    sum_num = 0
    print("pass : ", end="")
    if start < end:
        for count in range(start, end+1):
            if count%2 == 0:
                print(count, end=" ")
                sum_num += count
    else:
        for count in range(start, end-1, -1):
            if count%2 == 0:
                print(count, end=" ")
                sum_num += count
    print("\nSum : %d" %sum_num)
main(int(input()), int(input()))
