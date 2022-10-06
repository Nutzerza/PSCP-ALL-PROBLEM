"""Run Length Decoding"""
def main(txt):
    """print ans"""
    output = ""
    num = ""
    for word in txt:
        if word.isnumeric():
            num += word
        else:
            output += word*int(num)
            num = ""
    print(output)
main(input())
