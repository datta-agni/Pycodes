#Pattern:
#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5

rows= int(input("ENTER THE NUMBER OF ROWS"))
for num in range(rows):

    for i in range(num):

        print(num, end=" ")
        # print number

    # line after each row to display pattern correctly

    print()