# We import both methods from our custom 'roots' module.
from roots import bisection_method, newton_raphson_method

# Sample test equation: f(x) = x^2 - 4
def test_equation(x):
    return x**2 -4

print("Testing Bisection Method:")

# We execute the algorithm to search for a root within the [0, 5] interval.
print("Root found using Bisection Method, interval ([0,5]):")
root_bisect = bisection_method(test_equation, 0, 5)

if root_bisect is not None:
    print(f"Root found: {root_bisect}")

# We execute the algorithm starting from an initial guess of x0 = 5.
print("\nTesting Newton-Raphson Method, starting point (5):")
root_nr = newton_raphson_method(test_equation, 5)

if root_nr is not None:
    print(f"Root found: {root_nr}")