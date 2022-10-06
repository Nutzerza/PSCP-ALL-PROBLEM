"""Calculator"""
def total_press(num):
    """total press"""
    total = num
    if num == 1:
        total = 0

    for counter in range(1, num+1):
        total += len(str(counter))
    return total

def print_ans(num):
    """print ans"""
    ans = total_press(num)
    print(ans)

print_ans(int(input()))
