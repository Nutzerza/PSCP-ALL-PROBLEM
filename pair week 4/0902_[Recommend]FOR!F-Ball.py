"""[Recommend] FOR!F-Ball"""
def main(pos_change):
    """print ans"""
    box_a, box_b, box_c = "ball", "", ""
    for word in pos_change:
        if word == "A":
            box_a, box_b = box_b, box_a
        elif word == "B":
            box_b, box_c = box_c, box_b
        elif word == "C":
            box_a, box_c = box_c, box_a

    if box_a == "ball":
        print(1)
    elif box_b == "ball":
        print(2)
    elif box_c == "ball":
        print(3)

main(input())
