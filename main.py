"""
Main execution script for testing numerical analysis algorithms.
Includes tests for root-finding (Bisection, Newton-Raphson) 
and linear system solvers (Gaussian Elimination).
"""

# Import all our custom modules.
from roots import bisection_method, newton_raphson_method
from linear_systems import gauss_elimination

# ==========================================
# PART 1: ROOT FINDING ALGORITHMS
# ==========================================
print("--- 1. ROOT FINDING ALGORITHMS ---")

# Sample test equation: f(x) = x^2 - 4.
def test_equation(x):
    return x**2 - 4

root_bisect = bisection_method(test_equation, 0, 5)
if root_bisect is not None:
    print(f"Bisection Method Result: {root_bisect}")

root_nr = newton_raphson_method(test_equation, 5)
if root_nr is not None:
    print(f"Newton-Raphson Method Result: {root_nr}\n")


# ==========================================
# PART 2: LINEAR EQUATION SYSTEMS
# ==========================================
print("--- 2. LINEAR EQUATION SYSTEMS ---")
print("Solving the following system:")
print("2x + y = 5")
print("4x + 3y = 13")

# We define the matrix A (coefficients) and vector b (constants).
A = [
    [2.0, 1.0],
    [4.0, 3.0]
]
b = [5.0, 13.0]

# Execute the Gaussian Elimination algorithm.
solution = gauss_elimination(A, b)

if solution is not None:
    print(f"\nSolution Found: x = {solution[0]}, y = {solution[1]}")