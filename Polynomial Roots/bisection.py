# import necessary libraries
import sys
import time


def func_input():
    """
    Function to take input of a polynomial from user

    Returns:
    coeffs: list of coefficients of the polynomial
    """

    try:
        n = int(input("Enter degree of the polynomial: "))
        coeffs = [0] * (n + 1)
        for i in range(n):
            coeffs[i] = float(input(f'Coefficient of x^{n-i}: '))
        coeffs[n] = float(input(f'Constant term: '))
        
        func = 'f(x) = '
        for i in range(len(coeffs) - 1):
            if i == 0:
                func += f'{coeffs[i]}x^{n-i} '
                continue
            if coeffs[i] > 0:
                func += f'+ {coeffs[i]}x^{n-i} '
                continue
            if coeffs[i] < 0:
                func += f'{coeffs[i]}x^{n-i} '
                continue
            if coeffs[i] == 0:
                continue
        if coeffs[-1] > 0:
            func += f'+ {coeffs[-1]} '
        elif coeffs[-1] < 0:
            func += f'{coeffs[-1]} '
        else:
            pass

        sys.stdout.write(f'Input function is {func}\n')
        return coeffs

    # raise exception if input is invalid
    except ValueError:
        raise Exception("Input not a number")
    

def f(coeffs, x):
    """
    Function to evaluate the value of a polynomial at a given point

    Parameters:
    coeffs: list of coefficients of the polynomial
    x: point at which the polynomial is to be evaluated

    Returns:
    value: value of the polynomial at x
    """

    value = 0
    deg = len(coeffs) - 1
    for i, c in enumerate(coeffs):
        value += c * pow(x, (deg - i))

    return value


def bisect(coeffs, a, b, tolerance):
    """
    Function to find a root of a polynomial using bisection method

    Parameters:
    coeffs: list of coefficients of the polynomial
    a: first bound
    b: second bound
    tolerance: error tolerance

    Returns:
    mid: approximate root of the polynomial
    """

    bisect.iterations += 1

    if f(coeffs, a) * f(coeffs, b) > 0:
        raise Exception(f'Scalars {a} and {b} do not bound a root')
    
    mid = (a + b) / 2
    if abs(f(coeffs, mid)) < tolerance:
        return mid
    elif f(coeffs, a) * f(coeffs, mid) > 0:
        return bisect(coeffs, mid, b, tolerance)
    elif f(coeffs, b) * f(coeffs, mid) > 0:
        return bisect(coeffs, a, mid, tolerance)


# Driver code
if __name__ == '__main__':

    coefficients = func_input()
    try:
        a = float(input("Enter first bound: "))
        b = float(input("Enter second bound: "))
        tolerance = float(input("Error tolerance value: "))
    
    except ValueError:
        raise Exception(f'{a}, {b}, {tolerance} all need to be floating point numbers')
    
    # Define a global variable to count the number of iterations
    bisect.iterations = 0
    start = time.time()
    root = bisect(coefficients, a, b, tolerance)
    end = time.time() - start
    sys.stdout.write(f'Approximate root of f(x) = {root}\n')
    sys.stdout.write(f'Iterations to achieve the error tolerance = {bisect.iterations}\n')
    sys.stdout.write(f'Time taken for execution = {end} seconds\n')
