# Print Function
def my_print(n):
    for i in range(1,n+1):
        print(i, end="")

if __name__ == '__main__':
    n = int(input())
    my_print(n)