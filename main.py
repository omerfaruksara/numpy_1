# We import the Bisection method from our custom 'roots' module.
from roots import bisection_method

# We execute the algorithm to search for a root within the [0, 5] interval.
def test_equation(x):
    return x**2 -4

print("Testing the Bisection Method...\n")

root = bisection_method(test_equation, 0, 5)

# We check if a valid root was found before displaying the results.
if root is not None:
    print(f"Root found: {root}\n")
    print(f"Function value at root: {test_equation(root)}")