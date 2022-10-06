"""Stair"""
def check_high_step(max_high, step, step_1, counter, num_step):
    """check high step"""
    if max_high == step + step_1:
        ans = 1
        step = 0
    elif max_high < step + step_1:
        ans = 1
        step = step_1
    elif counter + 1 == num_step:
        ans = 1
        step = 0
    elif max_high > step + step_1:
        step = step + step_1
        ans = 0
    return ans, step

def check_can_step(step, max_high, can_up_stair):
    """check can step"""
    if step > max_high:
        return True
    elif step <= max_high and can_up_stair == True:
        return True

def main(max_high, num_step):
    """print ans"""
    can_up_stair = False
    step = 0
    total = 0
    for counter in range(num_step):
        step_1 = int(input())
        can_up_stair = check_can_step(step_1, max_high, can_up_stair)
        ans, step = check_high_step(max_high, step, step_1, counter, num_step)
        total += ans
        if step != 0 and counter +1 == num_step:
            total += 1

    if can_up_stair == True:
        print("NO")
    else:
        print(total)
main(int(input()), int(input()))
