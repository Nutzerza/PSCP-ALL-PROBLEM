"""[Recommend] EuclideanDistance2D"""
def calculator(num_q1, num_q2, num_p1, num_p2):
    """cal num"""
    return ((num_p1-num_q1)**2 + (num_p2-num_q2)**2)**0.5

def main(num_q1, num_q2, num_p1, num_p2):
    """print ans"""
    print(calculator(num_q1, num_q2, num_p1, num_p2))

main(float(input()), float(input()), float(input()), float(input()))
