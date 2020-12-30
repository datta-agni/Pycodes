#Unique Pyramid Pattern of Digits
#Pattern:
#1 
#1 2 1 
#1 2 3 2 1 
#1 2 3 4 3 2 1 
#1 2 3 4 5 4 3 2 1

rows = int(input("ENTER THE NUMBERS:"))

for i in range(1, rows + 1):

    for j in range(1,--i):

        print(j, end=" ")

    for j in range(--i, 0, -1):

        print(j, end=" ")

    print('')