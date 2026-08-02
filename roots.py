import numpy as np

# Bisection method for finding roots of a function
def bisection_method(func, a, b, tol = 1e-5, max_iter=100):

    #We check whether the product of the boundaries where we will begin the search is negative.
    if func(a) * func(b) >= 0:
        print("Bisection method fails. The function must have different signs at the endpoints a and b.")
        return None

    iter_count = 0

    #We check whether the division of the difference of the boundaries is greater than zero.
    while (b-a) / 2 > tol and iter_count < max_iter:

        #We are calculating the midpoint.
        c = (a+b) / 2

        #We check whether the function value at the midpoint is zero, which means we have found the root.
        if func(c)== 0:
            return c
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c

        #We increment the iteration count.
        iter_count += 1

    #If the maximum number of iterations is reached, we return the midpoint as the best estimate of the root.
    return (a+b) / 2

# We calculate the derivative numerically using a very small step size (h).
def numerical_derivative(func, x, h=1e-5):
    #Calculates the derivative of a function at a given point using numerical approximation.
    return (func(x+h) - func(x)) / h

# Newton-Raphson method for finding roots of a function.
def newton_raphson_method(func, x0, tol=1e-5, max_iter=100):
    iter_count = 0
    x = x0

    # We iterate until the maximum number of iterations is reached.
    while iter_count < max_iter:
        f_x = func(x)

        # We check if we have found the exact root.
        if abs(f_x) < tol:
            return x

        f_prime_x = numerical_derivative(func, x)

        # We prevent division by zero in case the derivative is zero.
        if f_prime_x == 0:
            print("Derivative is zero. Newton-Raphson method fails.")
            return None

        x_new = x - (f_x / f_prime_x)

        # We check whether the step size is smaller than our tolerance.
        if abs(x_new - x) < tol:
            return x_new

        x = x_new
        iter_count += 1

    print("Maximum iterations reached without convergence.")
    return x