"""[Recommend] SumOfNumber"""
def main(want):
    """print ans"""
    sum_num = 0
    while True:
        num = int(input())
        if num == -1:
            break
        else:
            sum_num += num
            if sum_num == want:
                break
    print(sum_num)
main(int(input()))
