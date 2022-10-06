"""LargestNumber"""
def check_most(num_1, num_2):
    """check most"""
    if num_1 > num_2:
        return num_1
    else:
        return num_2

def main(txt_1, txt_2, txt_3):
    """get value print ans"""
    num_1, num_2 = int(txt_1+txt_2+txt_3), int(txt_1+txt_3+txt_2)
    num_3, num_4 = int(txt_2+txt_1+txt_3), int(txt_2+txt_3+txt_1)
    num_5, num_6 = int(txt_3+txt_1+txt_2), int(txt_3+txt_2+txt_1)
    most = check_most(num_1, num_2)
    most = check_most(most, num_3)
    most = check_most(most, num_4)
    most = check_most(most, num_5)
    most = check_most(most, num_6)
    print(most)
main(input(), input(), input())
