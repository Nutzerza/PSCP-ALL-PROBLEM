"""Shorten"""
def check_last(ans):
    """check last ans"""
    count = 1
    for cha in ans:
        if count == len(ans):
            return cha
        count += 1

def check_base(num_input, num_count, ans):
    """check num"""
    if num_input == -1 and ans.count(",") == 0 and ans.count("-") == 0: # 12
        pass
    elif num_input == -1:
        ans += str(num_count)
    elif num_count == num_input - 1:
        if check_last(ans) == " ":
            ans += str(num_count)
        if check_last(ans) != "-":
            ans += "-"
        num_count = num_input
    elif ans.count(",") == 0 and ans.count("-") == 0: #3 4 6 7 9
        ans += ", "
        num_count = num_input
    else:
        ans += str(num_count) + ", "
        num_count = num_input
    return num_count, ans

def main():
    """print ans"""
    num_base = num_count = int(input())
    ans = str(num_base)
    if ans != "-1": #11
        while True:
            num_input = int(input())
            if num_input == -1:
                num_count, ans = check_base(num_input, num_count, ans)
                break

            num_count, ans = check_base(num_input, num_count, ans)
    else:
        ans = ""
    print(ans)
main()
#1
#1 2 5 8 10 13 14 15 Passed
#3 4 6 7 9 12 Incorrect 11 Error

# 11 = ""
