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
        elif func(c)<0:
            a = c
        else:
            b = c

        #We increment the iteration count.
        iter_count += 1

    #If the maximum number of iterations is reached, we return the midpoint as the best estimate of the root.
    return (a+b) / 2