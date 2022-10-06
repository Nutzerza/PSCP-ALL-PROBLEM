"""ValidVar"""
def check_reserved(txt):
    """check reserved"""
    if txt == "if" or txt == "else" or txt == "elif" or txt == "while" or \
    txt == "for" or txt == "True" or txt == "False" or txt == "continue" or \
    txt == "break" or txt == "return" or txt == "is" or txt == "in" or \
    txt == "and" or txt == "or" or txt == "from" or txt == "as" or \
    txt == "pass" or txt == "not" or txt == "def" or txt == "None":
        return True
    else:
        return False

def main(num):
    """loop get value print ans"""
    for _ in range(num):
        txt = input()
        if (not txt.isidentifier()) or txt.isspace() or check_reserved(txt):
            print("Invalid")
        else:
            print("Valid")
main(int(input()))
# txt.isidentifier() or txt[0].isnumeric()
