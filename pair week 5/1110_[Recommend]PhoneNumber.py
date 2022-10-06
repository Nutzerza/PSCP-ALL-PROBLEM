"""[Recommend] PhoneNumber"""
def main(phone_num, in_out_thai):
    """print ans"""
    if in_out_thai == "International":
        phone_num = "+66"+phone_num[1:]
    print(phone_num[:-8], phone_num[-8:-4], phone_num[-4:])
main(input(), input())
