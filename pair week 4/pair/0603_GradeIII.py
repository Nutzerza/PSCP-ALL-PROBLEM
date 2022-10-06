'''Grade III'''
def main():
    '''working space'''
    subjects = int(input())
    total = 0
    for _ in range(subjects):
        points = float(input())
        if points >= 95:
            total += 4
        elif points >= 90:
            total += 3.5
        elif points >= 85:
            total += 3
        elif points >= 80:
            total += 2.5
        elif points >= 75:
            total += 2
        elif points >= 70:
            total += 1.5
        elif points >= 65:
            total += 1
        elif points >= 60:
            total += 0.5
        elif points >= 0:
            total += 0
    average = total / subjects
    print('%.2f' %average)

main()
