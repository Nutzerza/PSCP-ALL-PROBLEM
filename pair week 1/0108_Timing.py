"""Timing"""


def main(sec):
    """get value cal num print"""
    minutes = sec//60
    sec = sec % 60
    hour = minutes//60
    minutes = minutes % 60
    day = hour//24
    hour = hour % 24
    print(day, hour, minutes, sec)


main(int(input()))
