# import necessary libraries
import sys
import time

# Set the maximum number of iterations
MAX_ITERS = 1e6


def func_input():
    """
    Function to take input of a polynomial from user

    Returns:
    coeffs: list of coefficients of the polynomial
    """

    try:
        n = 2
        coeffs = [0] * (n + 1)
        for i in range(n):
            coeffs[i] = float(input(f'Coefficient of x^{n - i}: '))
            if coeffs[0] == 0:
                raise Exception(f'Coefficient of x^{n} cannot be 0 for degree {n} polynomial')
        coeffs[n] = float(input(f'Constant term: '))

        func = 'f(x) = '
        for i in range(len(coeffs) - 1):
            if i == 0:
                func += f'{coeffs[i]}x^{n - i} '
                continue
            if coeffs[i] > 0:
                func += f'+ {coeffs[i]}x^{n - i} '
                continue
            if coeffs[i] < 0:
                func += f'{coeffs[i]}x^{n - i} '
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


def phi(coeffs, x):
    """
    Function to evaluate the value of phi(x) at a given point

    Parameters:
    coeffs: list of coefficients of the polynomial
    x: point at which phi(x) is to be evaluated

    Returns:
    value: value of phi(x) at x
    """

    try:
        Nr = -1 * coeffs[-1]
        Dr = coeffs[0] * x + coeffs[1]
        return Nr / float(Dr)

    # raise exception if denominator is 0
    except:
        sys.stdout.write('Error: f(x) does not converge for the initial guess\n')
        sys.exit()


def iterative(coeffs, x0, tolerance):
    """
    Function to find the roots of a polynomial using the fixed-point iterative scheme

    Parameters:
    coeffs: list of coefficients of the polynomial
    x0: initial guess
    tolerance: error tolerance

    Returns:
    root: root of the polynomial
    """

    while iterative.iterations <= MAX_ITERS:
        b = phi(coeffs, x0)
        x0 = b
        if abs(f(coeffs, b)) < tolerance:
            return b
        iterative.iterations += 1


# Driver code
if __name__ == '__main__':
    try:
        sys.stdout.write("The program works only for quadratic polynomials\n")
        coefficients = func_input()
        a = float(input("Choose initial guess: "))
        tolerance = float(input("Error tolerance value: "))

    except ValueError:
        raise Exception(f'{a} and {tolerance} need to be floating point numbers')

    # Define a global variable to count the number of iterations
    iterative.iterations = 0
    start = time.time()
    root = iterative(coefficients, a, tolerance)
    print(root)
    end = time.time() - start
    if not root:
        sys.stdout.write(f'Scalar {a} fails to converge for fixed-point iterative scheme\n')
        sys.stdout.write('No root found\n')
    else:
        sys.stdout.write(f'Approximate root of f(x) = {root}\n')
        sys.stdout.write(f'Iterations to achieve the error tolerance = {iterative.iterations}\n')
        sys.stdout.write(f'Time taken for execution = {end} seconds\n')
