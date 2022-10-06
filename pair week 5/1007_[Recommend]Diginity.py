"""[Recommend] Diginity"""
def find_digit(num):
    """find digit"""
    total = counter = 0
    while len(num) > 1:
        total += int(num[counter])
        counter += 1
        if counter == len(num):
            num = str(total)
            total = counter = 0
    return num

def main():
    """get value print ans"""
    while True:
        num = input()
        if num == "0":
            break
        else:
            print(find_digit(num))
main()
