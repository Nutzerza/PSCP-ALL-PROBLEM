"""SecondConverter"""
def time(all_sec, sec_min, min_hour):
    """change time"""
    minute = all_sec // sec_min
    sec = all_sec % sec_min
    hour = minute // min_hour
    minute = minute % min_hour
    return hour, minute, sec

def main(all_sec, sec_min, min_hour, hour_day):
    """get value print ans"""
    sec_day = hour_day*min_hour*sec_min
    if all_sec // sec_day > 0:
        all_sec = all_sec % sec_day
    print("%d:%d:%d" %time(all_sec, sec_min, min_hour))

main(int(input()), int(input()), int(input()), int(input()))
