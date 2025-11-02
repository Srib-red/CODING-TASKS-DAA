n = int(input("Enter size of matrix: "))

matrix = []
for i in range(n):
    row = []
    for j in range(n):
        x = int(input(f"Enter element ({i+1}, {j+1}): "))
        row.append(x)
    matrix.append(row)

i = int(input("Specify the row: "))
j = int(input("Specify the column: "))

if 1 <= i <= n and 1 <= j <= n:
    print(f"Element ({i}, {j}): {matrix[i-1][j-1]}")
else:
    print("i and j should be between 1 and", n)

