if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if b != 0:
        print(a // b, end="\n")
        print(a / b, end="\n")
    else:
        print("Error: Division by zero")
