"""BMI"""
def bmi(weight, high):
    """cal bmi"""
    return weight/((high/100)**2)

def main():
    """print ans"""
    print("%s\'s  BMI = %.2f" %(input(), bmi(float(input()), float(input()))))
    print("%s\'s  BMI = %.2f" %(input(), bmi(float(input()), float(input()))))
    print("%s\'s  BMI = %.2f" %(input(), bmi(float(input()), float(input()))))
    print("%s\'s  BMI = %.2f" %(input(), bmi(float(input()), float(input()))))
    print("%s\'s  BMI = %.2f" %(input(), bmi(float(input()), float(input()))))
main()
