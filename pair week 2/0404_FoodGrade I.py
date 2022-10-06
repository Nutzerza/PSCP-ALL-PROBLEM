"""FoodGrade I"""
def check_weight(weight_1, weight_2):
    """check weight chicken"""
    if (weight_1 >= 50 and weight_1 <= 70) and (weight_2 >= 50 and weight_2 <= 70):
        return 2
    elif (weight_1 >= 50 and weight_1 <= 70) or (weight_2 >= 50 and weight_2 <= 70):
        return 1
    else:
        return 0

def main(num_wing=0):
    """cal check print ans"""
    num_wing += check_weight(int(input()), int(input()))
    num_wing += check_weight(int(input()), int(input()))
    num_wing += check_weight(int(input()), int(input()))
    num_wing += check_weight(int(input()), int(input()))
    num_wing += check_weight(int(input()), int(input()))
    num_wing += check_weight(int(input()), int(input()))
    num_wing += check_weight(int(input()), int(input()))
    num_wing += check_weight(int(input()), int(input()))
    num_wing += check_weight(int(input()), int(input()))
    num_wing += check_weight(int(input()), int(input()))
    num_wing += check_weight(int(input()), int(input()))
    num_wing += check_weight(int(input()), int(input()))
    print(num_wing)
main()
