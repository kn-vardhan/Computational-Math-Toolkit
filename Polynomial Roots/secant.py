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


def secant(coeffs, x1, x2, tolerance):
    """
    Function to find the root of a polynomial using secant method

    Parameters:
    coeffs: list of coefficients of the polynomial
    x1: first initial guess
    x2: second initial guess
    tolerance: error tolerance value

    Returns:
    xm1: approximate root of the polynomial
    """
    
    xm1 = 0
    xm2 = 0
    flag = 0

    # check if the initial guesses are valid
    if f(coeffs, x1) * f(coeffs, x2) < 0:
        while 1:
            xm1 = (x1 * f(coeffs, x2) - x2 * f(coeffs, x1)) / (f(coeffs, x2) - f(coeffs, x1))
            flag = f(coeffs, x1) * f(coeffs, xm1)
            if flag == 0:
                break
            
            secant.iterations += 1
            x1 = x2
            x2 = xm1
            xm2 = (x1 * f(coeffs, x2) - x2 * f(coeffs, x1)) / (f(coeffs, x2) - f(coeffs, x1))
            if abs(xm2 - xm1) < tolerance:
                break
            
        return xm1

    else:
        return None


# Driver code
if __name__ == '__main__':
    
    try:
        coefficients = func_input()
        x1 = float(input("Choose initial guess x1: "))
        x2 = float(input("Choose initial guess x2: "))
        tolerance = float(input("Error tolerance value: "))
    except ValueError:
        raise Exception(f'{x1}, {x2}, {tolerance} all need to be floating point numbers')
    
    # Define a global variable to count the number of iterations
    secant.iterations = 0
    start = time.time()
    root = secant(coefficients, x1, x2, tolerance)
    end = time.time() - start
    if root:
        sys.stdout.write(f'Approximate root of f(x) = {root}\n')
        sys.stdout.write(f'Iterations to achieve the error tolerance = {secant.iterations}\n')
        sys.stdout.write(f'Time taken for execution = {end} seconds\n')
    else:
        sys.stdout.write(f'Scalars {x1} and {x2} do not converge for root\n')
        sys.stdout.write('No root found\n')
