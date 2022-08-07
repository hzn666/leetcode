if __name__ == '__main__':
    string = input()

    for i in range(0, len(string), 8):
        print(string[i:i + 8] + "0" * (8 - len(string[i:i + 8])))
