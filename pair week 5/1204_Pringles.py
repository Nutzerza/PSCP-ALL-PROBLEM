"""Pringles"""
def main(can_top, pringles, can_bottom, want):
    """print ans ปล.เดี๋ยวหาวิธีแก้ได้และจะกลับมาแก้เละเกิ๊น"""
    get_pringles = 0
    void = ""
    for counter in range(want):
        if pringles[counter] == ")":
            get_pringles += 1
        void += " "
        left_pringles = pringles[counter+1:]

    print(get_pringles)
    if left_pringles.count(")") != 0:
        print("There are still some left.")
    else:
        print("None.")
    print(can_top)
    print(void + left_pringles)
    print(can_bottom)
main(input(), input(), input(), int(input()))
