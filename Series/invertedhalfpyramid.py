#Inverted Half Pyramid Number Pattern
#Pattern:
#0 1 2 3 4 5 
#0 1 2 3 4 
#0 1 2 3 
#0 1 2 
#0 1

rows = int(input("ENTER THE NUMBER OF ROWS:"))

for i in range(rows, 1, -1):

    for j in range(1, i + 1):

        print(j, end=" ")

    print("\r")