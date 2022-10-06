"""Grade III"""
def get_sum_grade(num):
    """sum grade"""
    sum_grade = 0
    for _ in range(num):
        score = float(input())
        if score >= 95:
            sum_grade += 4.0
        elif score >= 90:
            sum_grade += 3.5
        elif score >= 85:
            sum_grade += 3.0
        elif score >= 80:
            sum_grade += 2.5
        elif score >= 75:
            sum_grade += 2.0
        elif score >= 70:
            sum_grade += 1.5
        elif score >= 65:
            sum_grade += 1.0
        elif score >= 60:
            sum_grade += 0.5
        else:
            sum_grade += 0
    return sum_grade

def main(num):
    """print ans"""
    avg = get_sum_grade(num)/num
    output = int(avg*100) / 100
    print("%.2f" %output)
main(int(input()))
