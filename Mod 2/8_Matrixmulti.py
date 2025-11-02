# Matrix Multiplication - User Input Version

# Function to take matrix input
def input_matrix(name):
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))

    print(f"Enter elements of {name} row by row:")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            x = int(input(f"Enter element ({i+1}, {j+1}): "))
            row.append(x)
        matrix.append(row)
    
    return matrix, rows, cols  # ✅ must return


# Function to multiply matrices
def multiply_matrices(A, B):
    # Initialize result matrix with zeros
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # Matrix multiplication logic
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result


# --- Main Program ---
A, r1, c1 = input_matrix("Matrix A")
B, r2, c2 = input_matrix("Matrix B")

# Check if multiplication is possible
if c1 != r2:
    print(" Matrix multiplication not possible! Columns of A must equal rows of B.")
else:
    product = multiply_matrices(A, B)
    print("\n Product of matrices:")
    for row in product:
        print(row)
