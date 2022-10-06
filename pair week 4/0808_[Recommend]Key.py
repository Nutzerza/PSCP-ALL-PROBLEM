"""[Recommend] Key"""
def main(txt):
    """print ans"""
    sum_to_thirteen = 0
    for word in txt:
        sum_to_thirteen += int(word)
    sum_three_last = int(txt[-3:])*10
    total = sum_three_last + sum_to_thirteen
    if total < 1000:
        print(total+1000)
    elif total >= 10000:
        print(str(total)[-4:])
    else:
        print(total)
main(input())
