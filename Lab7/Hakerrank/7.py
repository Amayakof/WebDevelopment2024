# Text Alignment
# Top pyramid
def top_pyramid(thickness):
    for i in range(thickness):
        print(('H' * i).rjust(thickness - 1) + 'H' + ('H' * i).ljust(thickness - 1))

# Top
def top(thickness):
    for i in range(thickness + 1):
        print(('H' * thickness).center(thickness * 2) + ('H' * thickness).center(thickness * 6))

# Mid
def mid(thickness):
    for i in range((thickness + 1) // 2):
        print(('H' * (thickness * 5)).center(thickness * 6))  # Fixed indentation here

# Bottom
def bottom(thickness):
    for i in range(thickness + 1):
        print(('H' * thickness).center(thickness * 2) + ('H' * thickness).center(thickness * 6))


def bottom_pyramid(thickness):
    for i in range(thickness):
        print(('H' * (thickness - i - 1)).rjust(thickness * 5) + 'H' + ('H' * (thickness - i - 1)).ljust(thickness * 4))


if __name__ == '__main__':
    thickness = int(input())
    top_pyramid(thickness)
    top(thickness)
    mid(thickness)
    bottom(thickness)
    bottom_pyramid(thickness)
