"""robot I"""

def main():
    """age and name"""
    name = input()
    age = float(input())
    if age < 18:
        print(name+", you can pass.")
    else:
        print(name+", you shall not pass.")
main()
    