"""MAC"""
def check_valid(address):
    """check valid"""
    if (address.count("-") or address.count(":")) and len(address) != 17:
        return "error"
    elif address.count(".") and len(address) != 14:
        return "error"
    elif address.count("-") and address[2] == "-" and address[5] == "-" \
        and address[8] == "-" and address[11] == "-" and address[14] == "-":
        return "VALID 1"
    elif address.count(":") and address[2] == ":" and address[5] == ":" \
        and address[8] == ":" and address[11] == ":" and address[14] == ":":
        return "VALID 2"
    elif address.count(".") and address[4] == "." and address[9] == ".":
        return "VALID 3"
    else:
        return "error"

def check_base16(address):
    """check base 16"""
    num_base16 = "0123456789ABCDEF"
    for counter in range(len(address)):
        if address[counter] == "-" or address[counter] == ":" or address[counter] == ".":
            continue
        if address[counter] not in num_base16:
            return "error"

def main(address):
    """cal func nd print"""
    valid = check_valid(address)
    check_16 = check_base16(address)
    if valid == "error" or check_16 == "error":
        print("ERROR")
    else:
        print(valid)
main(input().upper())
