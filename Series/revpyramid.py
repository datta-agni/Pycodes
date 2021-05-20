# Reverse Pyramid of Numbers
# Pattern:
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

rows = int(input("ENTER THE NUMBER OF ROWS:"))

for row in range(1, rows):

    for column in range(row, 0, -1):
        print(column, end=" ")

    print("")
