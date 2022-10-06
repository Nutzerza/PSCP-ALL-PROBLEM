"""[Recommend] Virus I"""
def main(txt, count=0):
    """print ans"""
    for word in txt:
        if word == "o":
            count += 1
    print(count)
main(input())
