"""ProgressiveTax"""
def cal_15_30(income):
    """cal_15_30"""
    tax = 0
    if income > 300000:
        tax += 150000 * 0.05
    else:
        tax += (income - 150000) * 0.05
    return tax

def cal_30_50(income):
    """cal_30_50"""
    tax = 0
    if income > 500000:
        tax += 200000 * 0.10
    else:
        tax += (income - 300000) * 0.10
    return tax + cal_15_30(income)

def cal_50_75(income):
    """cal_50_75"""
    tax = 0
    if income > 750000:
        tax += 250000 * 0.15
    else:
        tax += (income - 500000) * 0.15
    return tax + cal_30_50(income)

def cal_75_100(income):
    """cal_75_100"""
    tax = 0
    if income > 1000000:
        tax += 250000 * 0.20
    else:
        tax += (income - 750000) * 0.20
    return tax + cal_50_75(income)

def cal_100_200(income):
    """cal_100_200"""
    tax = 0
    if income > 2000000:
        tax += 1000000 * 0.25
    else:
        tax += (income - 1000000) * 0.25
    return tax + cal_75_100(income)

def cal_200_400(income):
    """cal_200_400"""
    tax = 0
    if income > 4000000:
        tax += 2000000 * 0.30
    else:
        tax += (income - 2000000) * 0.30
    return tax + cal_100_200(income)

def cal_400_up(income):
    """cal_400_up"""
    tax = (income - 4000000) * 0.35
    return tax + cal_200_400(income)

def total_income(income):
    """sum income"""
    sum_income = 0
    if income > 4000000:
        sum_income += cal_400_up(income)
    elif income > 2000000:
        sum_income += cal_200_400(income)
    elif income > 1000000:
        sum_income += cal_100_200(income)
    elif income > 750000:
        sum_income += cal_75_100(income)
    elif income > 500000:
        sum_income += cal_50_75(income)
    elif income > 300000:
        sum_income += cal_30_50(income)
    elif income > 150000:
        sum_income += cal_15_30(income)
    else:
        sum_income += 0
    return sum_income

def main(income):
    """print ans"""
    cost = total_income(income)
    if cost == 0:
        print(0)
    else:
        print(int(cost))
main(float(input()))
