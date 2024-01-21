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


def f_derivative(coeffs):
    """
    Function to find the derivative of a polynomial

    Parameters:
    coeffs: list of coefficients of the polynomial

    Returns:
    new_coeffs: list of coefficients of the derivative of the polynomial
    """

    new_coeffs = []
    deg = len(coeffs) - 1
    for i, c in enumerate(coeffs):
        if deg - i <= 0:
            continue
        new_coeffs.append(c*(deg - i))

    return new_coeffs


def newton_raphson(coeffs, coeffs_der, coeffs_der_1, x0, tolerance):
    """
    Function to find the root of a polynomial using Newton-Raphson method

    Parameters:
    coeffs: list of coefficients of the polynomial
    coeffs_der: list of coefficients of the derivative of the polynomial
    coeffs_der_1: list of coefficients of the second derivative of the polynomial
    x0: initial guess
    tolerance: error tolerance

    Returns:
    x1: root of the polynomial
    """

    flag1 = f(coeffs_der, x0) == 0
    flag2 = abs(f(coeffs, x0) * f(coeffs_der_1, x0)) < pow(abs(f(coeffs_der, x0)), 2)
    
    # raise exception if initial guess is not valid
    if flag1:
        raise Exception(f'Scalar {x0} fails for Newton-Raphson method')
    
    while 1:
        x1 = x0 - f(coeffs, x0) / f(coeffs_der, x0)
        
        newton_raphson.iterations += 1
        if newton_raphson.iterations > MAX_ITERS:
            return None
        
        x0 = x1
        if abs(f(coeffs, x1)) < tolerance:
            break
    
    return x1


# Driver code
if __name__ == '__main__':
    
    try:
        coefficients = func_input()
        derivatives = f_derivative(coefficients)
        derivatives_1 = f_derivative(derivatives)
        x0 = float(input("Choose initial guess: "))
        tolerance = float(input("Error tolerance value: "))
    
    except ValueError:
        raise Exception(f'{x0}, {tolerance} need to be floating points numbers')

    # Define a global variable to count the number of iterations
    newton_raphson.iterations = 0
    start = time.time()
    root = newton_raphson(coefficients, derivatives, derivatives_1, x0, tolerance)
    end = time.time() - start
    if root:
        sys.stdout.write(f'Approximate root of f(x) = {root}\n')
        sys.stdout.write(f'Iterations to achieve the error tolerance = {newton_raphson.iterations}\n')
        sys.stdout.write(f'Time taken for execution = {end} seconds\n')
    else:
        sys.stdout.write(f'Scalar {x0} fails to converge for N-R method\n')
        sys.stdout.write('No root found\n')
