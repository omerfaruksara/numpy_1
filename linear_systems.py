"""
Module for solving systems of linear equations.
Currently implements the Gaussian Elimination algorithm.
"""

def gauss_elimination(A, b):
    n = len(b)

    #Forward Elimination with Partial Pivoting.
    for i in range(n):

        # Find the row with the largest absolute value in the current column.
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k

        # Swap the current row with the max_row to minimize rounding errors.
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]

        # Check for singular matrix to prevent division by zero.
        if A[i][i] == 0:
            print("matrix is singular. cannot find a unique solution.")
            return None

        # Eliminate variables below the current pivot.
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]

    # Back Substitution to find the solution vector x.
    x = [0] * n
    for i in range(n - 1, -1, -1):
        sum_ax = 0
        for j in range(i + 1, n):
            sum_ax += A[i][j] * x[j]

        #Calculate the final value for the current variable.
        x[i] = (b[i] - sum_ax) / A[i][i]

    return x
        