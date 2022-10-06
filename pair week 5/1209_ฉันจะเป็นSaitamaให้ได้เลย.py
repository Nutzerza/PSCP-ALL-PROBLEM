"""ฉันจะเป็น Saitama ให้ได้เลย"""
from math import ceil

def main():
    """print ans"""
    want_pushups, want_situp = int(input()), int(input())
    want_stand_sit, want_run = int(input()), int(input())
    most_pushups, most_situp = int(input()), int(input())
    most_run, most_stand_sit = int(input()), int(input())

    most_day = 0
    if most_day < want_pushups / most_pushups:
        most_day = want_pushups / most_pushups
    if most_day < want_situp / most_situp:
        most_day = want_situp / most_situp
    if most_day < want_stand_sit / most_stand_sit:
        most_day = want_stand_sit / most_stand_sit
    if most_day < want_run / most_run:
        most_day = want_run / most_run

    print("%d" %(ceil(most_day)))
main()
