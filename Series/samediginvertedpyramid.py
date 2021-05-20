# Inverted Pyramid of the Same Digit
# Pattern:
# 5 5 5 5 5
# 5 5 5 5
# 5 5 5
# 5 5
# 5

rows = int(input("ENTER THE NUMBER OF ROWS"))

num = rows

for i in range(rows, 0, -1):

    for j in range(0, i):
        print(num, end=" ")

    print("\r")
