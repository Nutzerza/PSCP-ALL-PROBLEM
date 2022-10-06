"""BigFrame"""
def check_most_len(num_1, num_2):
    """check_most_len"""
    if num_1 > num_2:
        return num_1
    else:
        return num_2

def main(txt_1, txt_2, txt_3, txt_4, txt_5):
    """print ans""" # ขอผ่านก่อนนะ
    most_len = check_most_len(len(txt_1), len(txt_2))
    most_len = check_most_len(most_len, len(txt_3))
    most_len = check_most_len(most_len, len(txt_4))
    most_len = check_most_len(most_len, len(txt_5))

    #แก้
    print("*"*(most_len+4))
    print("* " + txt_1 + " "*(most_len-len(txt_1)) + " *")
    print("* " + txt_2 + " "*(most_len-len(txt_2)) + " *")
    print("* " + txt_3 + " "*(most_len-len(txt_3)) + " *")
    print("* " + txt_4 + " "*(most_len-len(txt_4)) + " *")
    print("* " + txt_5 + " "*(most_len-len(txt_5)) + " *")
    print("*"*(most_len+4))

main(input().strip(), input().strip(), input().strip(), input().strip(), input().strip())

    # เก่า
    # for row in range(7):
    #     for col in range(most_len+4):
    #         if row == 0 or row == 6 or col == 0 or col == most_len+3:
    #             print("*", end="")
    #         elif row == 1 and col >= 2 and col <= len(txt_1)+1:
    #             print(txt_1[col-2], end="")
    #         elif row == 2 and col >= 2 and col <= len(txt_2)+1:
    #             print(txt_2[col-2], end="")
    #         elif row == 3 and col >= 2 and col <= len(txt_3)+1:
    #             print(txt_3[col-2], end="")
    #         elif row == 4 and col >= 2 and col <= len(txt_4)+1:
    #             print(txt_4[col-2], end="")
    #         elif row == 5 and col >= 2 and col <= len(txt_5)+1:
    #             print(txt_5[col-2], end="")
    #         else:
    #             print(" ", end="")
    #     print()
