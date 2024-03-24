# Text Alignment
thickness = int(input())

# Top Cone
for i in range(thickness):
    # Print 'H' aligned to the center with width (2 * thickness - 1)
    print(('H' * i).rjust(thickness - 1) + 'H' + ('H' * i).ljust(thickness - 1))

# Top Pillars
for i in range(thickness + 1):
    # Print 'H' aligned to the center with width (thickness * 2)
    print(('H' * thickness).center(thickness * 2) + ('H' * thickness).center(thickness * 6))

# Middle Belt
for i in range((thickness + 1) // 2):
    # Print 'H' aligned to the center with width (thickness * 6)
    print(('H' * (thickness * 5)).center(thickness * 6))

# Bottom Pillars
for i in range(thickness + 1):
    # Print 'H' aligned to the center with width (thickness * 2)
    print(('H' * thickness).center(thickness * 2) + ('H' * thickness).center(thickness * 6))

# Bottom Cone
for i in range(thickness):
    # Print 'H' aligned to the center with width (2 * thickness - 1)
    print(('H' * (thickness - i - 1)).rjust(thickness) + 'H' + ('H' * (thickness - i - 1)).ljust(thickness))
