"""BMIAgain"""
def cal_bmi(weight, high_cm):
    """Calculate BMI"""
    return weight/(high_cm/100)**2

def check(bmi):
    """Check BMI"""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main(weight, high_cm):
    """print ans"""
    print(check(cal_bmi(weight, high_cm)))

main(int(input()), int(input()))
