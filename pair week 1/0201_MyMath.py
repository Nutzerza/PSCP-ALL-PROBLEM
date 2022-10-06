"""MyMath"""
import math
def main():
    """cal num print ans"""
    print((math.sin(math.radians(90))+math.sin(math.radians(60))**2)/ \
    (math.cos(math.radians(245**2))+math.cos(math.radians(45+135))))
    print((math.factorial(16)*math.factorial(4))/math.factorial(8))
    print((15+25)/((25-12)**2+(12-15)**2)**0.5)
    print(math.log10(1234**4))
    print(((math.log(4234)/math.log(5))+(math.log(8191)/math.log(2))+\
        (71*math.log10(156154)))/((math.log(777)/math.log(7))-\
        (math.log(888)/math.log(8))-(math.log(999)/math.log(9))))
main()
