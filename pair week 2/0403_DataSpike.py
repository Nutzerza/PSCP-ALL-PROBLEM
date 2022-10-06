"""DataSpike"""
def check_most_data(data_1, data_2):
    """check most data"""
    if data_1 <= data_2:
        return data_2
    elif data_1 > data_2:
        return data_1

def main():
    """print ans"""
    most_data = check_most_data(int(input()), int(input()))
    most_data = check_most_data(int(input()), most_data)
    most_data = check_most_data(int(input()), most_data)
    most_data = check_most_data(int(input()), most_data)
    most_data = check_most_data(int(input()), most_data)
    most_data = check_most_data(int(input()), most_data)
    most_data = check_most_data(int(input()), most_data)
    print(most_data)

main()
