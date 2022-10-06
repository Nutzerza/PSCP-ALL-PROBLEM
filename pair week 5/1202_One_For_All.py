"""One For All"""
def main(num):
    """loop for get value print ans"""
    ans = ""
    for counter in range(1, num+1):
        name = input()
        if counter == num:
            ans += name + "_%d" %counter
        elif counter%2:
            ans += name + "*"*counter
        else:
            ans += name + "-"*counter
    print(ans)
main(int(input()))
