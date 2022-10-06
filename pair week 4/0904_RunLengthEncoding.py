"""Run Length Encoding"""
def main(txt):
    """print ans"""
    count = 1
    ans = ""
    for num in range(len(txt)):
        if num == len(txt)-1:
            ans += str(count) + txt[num]
        if num+1 < len(txt) and txt[num] != txt[num+1]:
            ans += str(count) + txt[num]
            count = 1
        else:
            count += 1
    print(ans)
main(input())
