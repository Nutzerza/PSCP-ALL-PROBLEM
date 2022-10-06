"""Meteorite"""
def total_missile(weight_first, rupture, weight_safe):
    """total missile"""
    weight = weight_first
    total = 0
    counter = 0
    while weight >= weight_safe:
        total += rupture  ** counter
        weight = weight / rupture
        counter += 1
    return total

def print_ans(weight_first, rupture, weight_safe):
    """print ans"""
    print(total_missile(weight_first, rupture, weight_safe))
print_ans(float(input()), int(input()), float(input()))
