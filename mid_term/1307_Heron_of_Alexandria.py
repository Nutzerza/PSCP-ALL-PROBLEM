"""Heron of Alexandria"""
def calculate(num_a, num_b, num_c):
    """calculate"""
    num_s = (num_a + num_b + num_c) / 2
    return (num_s * (num_s - num_a) * (num_s - num_b) * (num_s - num_c))**0.5

def print_ans(num_a, num_b, num_c):
    """print ans"""
    print("%.3f" %calculate(num_a, num_b, num_c))

print_ans(float(input()), float(input()), float(input()))
