"""Day I"""
def main(chris_era):
    """print ans"""
    if chris_era % 4 != 0 or (chris_era % 100 == 0 and chris_era % 400 != 0):
        print("No")
    else:
        print("Yes")
main(int(input()))
