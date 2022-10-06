"""Parity"""
def count_num_1(set_num):
    """count num 1"""
    total_num_1 = 0
    for cha in set_num:
        if cha == "1":
            total_num_1 += 1
    return total_num_1

def check_con_return_ans(set_num, con):
    """check con return ans"""
    total_num_1 = count_num_1(set_num)
    if total_num_1 % 2 and con == "Even":
        ans = set_num + "1"
    elif total_num_1 % 2 and con == "Odd":
        ans = set_num + "0"
    elif con == "Even":
        ans = set_num + "0"
    else:
        ans = set_num + "1"
    return ans

def print_ans(set_num, con):
    """print ans"""
    ans = check_con_return_ans(set_num, con)
    print(ans)
print_ans(input(), input())
