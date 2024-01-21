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
            coeffs[i] = float(input(f'Coefficient of x^{n - i}: '))
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


def f_derivative(coeffs):
    """
    Function to calculate the derivative of a polynomial

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
        new_coeffs.append(c * (deg - i))

    return new_coeffs


def degree(poly):
    """
    Function to calculate the degree of a polynomial

    Parameters:
    poly: list of coefficients of the polynomial

    Returns:
    len(poly)-1: degree of the polynomial
    """

    while poly and poly[-1] == 0:
        poly.pop()
    return len(poly)-1


def poly_div(Nr, Dr):
    """
    Function to divide two polynomials

    Parameters:
    Nr: list of coefficients of the numerator polynomial
    Dr: list of coefficients of the denominator polynomial

    Returns:
    rem: list of coefficients of the remainder polynomial
    """

    Nr = Nr[::-1]
    Dr = Dr[::-1]

    # Get the degrees of the polynomials
    deg_Dr = degree(Dr)
    deg_Nr = degree(Nr)

    if deg_Dr < 0:
        return [0]

    if deg_Nr >= deg_Dr:
        quo = [0] * deg_Nr
        while deg_Nr >= deg_Dr:
            d = [0] * (deg_Nr - deg_Dr) + Dr
            mult = quo[deg_Nr - deg_Dr] = Nr[-1] / float(d[-1])
            d = [c * mult for c in d]
            Nr = [c_Nr - c_Dr for c_Nr, c_Dr in zip(Nr, d)]
            deg_Nr = degree(Nr)
        rem = Nr
    else:
        quo = [0]
        rem = Nr

    return rem


def sturm(all_funcs, breakpoints):
    """
    Function to calculate the number of real roots of a polynomial in a given interval

    Parameters:
    all_funcs: list of lists of coefficients of the polynomial and its derivatives
    breakpoints: list of breakpoints

    Returns:
    sign_changes: list of tuples of breakpoints and number of real roots between them
    """

    func1 = all_funcs[0].copy()
    func2 = all_funcs[1].copy()
    temp = poly_div(func1, func2)[::-1]
    temp = [round(-1 * x, 3) for x in temp]
    all_funcs.append(temp)

    while len(temp) != 1:
        func1 = all_funcs[-2].copy()
        func2 = all_funcs[-1].copy()
        temp = poly_div(func1, func2)[::-1]
        temp = [round(-1 * x, 3) for x in temp]
        all_funcs.append(temp)

    all_funcs = list(filter(None, all_funcs))
    if all_funcs[-1] == [0]:
        all_funcs.pop()

    # Dictionary to store number of sign changes
    sign_changes = {}
    for point in breakpoints:
        prev = cur = None
        count = 0
        for i, func in enumerate(all_funcs):
            if f(func, point) > 0:
                cur = True
                if i != 0 and prev != cur:
                    count += 1
            elif f(func, point) < 0:
                cur = False
                if i != 0 and prev != cur:
                    count += 1
            else:
                continue
            prev = cur
        sign_changes[point] = count

    # Sort the dictionary by first element - breakpoint
    sign_changes = sorted(sign_changes.items(), key=lambda x: x[0])
    return sign_changes


def print_loc(sign_changes):
    """
    Function to print the number of real roots of a polynomial in a given interval

    Parameters:
    sign_changes: list of tuples of breakpoints and number of real roots between them

    Returns:
    None
    """

    for i in range(len(sign_changes) - 1):
        diff = abs(sign_changes[i][1] - sign_changes[i + 1][1])
        sys.stdout.write(f'{diff} real root(s) b/w ({sign_changes[i][0]}, {sign_changes[i+1][0]})\n')


# Driver code
if __name__ == '__main__':
    try:
        coefficients = func_input()
        derivatives = f_derivative(coefficients)
        seq = [coefficients, derivatives]
        b = int(input("Enter number of break points: "))
        if not b > 1:
            raise Exception(f'Invalid input: number of break points needs to a positive integer')
        breaks = []
        idx = 1
        while idx <= b and b > 1:
            breaks.append(float(input(f'Enter break point {idx}: ')))
            idx += 1
        breaks = sorted(list(set(breaks)))

    except ValueError:
        raise Exception(f'Invalid input')

    signs = sturm(seq, breaks)
    sys.stdout.write("Number of roots between the intervals are:\n")
    print_loc(signs)
