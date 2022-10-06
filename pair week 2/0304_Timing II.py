"""Timing"""

def main():
    """time"""
    sec = int(input())
    minu = sec//60
    sec = sec % 60
    hour = minu//60
    minu = minu % 60
    day = hour//24
    hour = hour % 24
    if day > 9999:
        print("ERR_:__:__:__")
    else:
        print("%04d:%02d:%02d:%02d" %(day, hour, minu, sec))
main()
