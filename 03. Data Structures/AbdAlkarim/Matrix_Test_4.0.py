import random
matrix = []
total = 0
numberOfRows = eval(input("Enter the number of rows: "))
numberOfColumns = eval(input("Enter the number of columns: "))
for row in range(0, numberOfRows):
    matrix.append([])
    for colimns in range(0, numberOfColumns):
        matrix[row].append(random.randrange(0,100))
        total += matrix[row][colimns]

print("total is " + str(total))
print(matrix)