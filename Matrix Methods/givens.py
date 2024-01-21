# import necessary libraries
import numpy as np
import time


def inputMatrix():
    """
    Function to take input of augmented matrix from user

    Returns:
    mat: augmented matrix
    M: number of variables
    """


    try:
        n = int(input("Enter the number of rows in the square matrix: "))
    except ValueError:
        raise Exception(f'Invalid input: Rows of a square matrix need to be positive integers')
    if n < 1:
        raise Exception(f'Invalid input: Rows of a square matrix need to be positive integers')

    mat = []
    try:
        for i in range(n):
            if i == 0:
                row = input(f'Enter elements of {i+1}st row: ').split()
                row = [float(x) for x in row]
                if len(row) != n:
                    raise Exception(f'Invalid input - Each row should contain {n} element(s), input has {len(row)} element(s)')
            elif i == 1:
                row = input(f'Enter elements of {i+1}nd row: ').split()
                row = [float(x) for x in row]
                if len(row) != n:
                    raise Exception(f'Invalid input - Each row should contain {n} element(s), input has {len(row)} element(s)')
            elif i == 2:
                row = input(f'Enter elements of {i+1}rd row: ').split()
                row = [float(x) for x in row]
                if len(row) != n:
                    raise Exception(f'Invalid input - Each row should contain {n} element(s), input has {len(row)} element(s)')
            else:
                row = input(f'Enter elements of {i+1}th row: ').split()
                row = [float(x) for x in row]
                if len(row) != n:
                    raise Exception(f'Invalid input - Each row should contain {n} element(s), input has {len(row)} element(s)')
            
            mat.append(row)
        
        return mat, n
    
    # raise exception if input is invalid
    except ValueError:
        raise Exception(f'Invalid input - Elements of a matrix should be floating point numbers')


def func(coeffs, x):
    """
    Function to evaluate the value of a polynomial at a given point

    Parameters:
    coeffs: list of coefficients of the polynomial
    x: point at which the polynomial is to be evaluated

    Returns:
    value: value of the polynomial at x
    """

    coeffs = coeffs[::-1]
    value = 0
    deg = len(coeffs) - 1
    for i, c in enumerate(coeffs):
        value += c * pow(x, (deg - i))
    return value


def secant(coeffs, x1, x2, tolerance):
    """
    Function to find the roots of a polynomial using the secant method

    Parameters:
    coeffs: list of coefficients of the polynomial
    x1: first initial guess
    x2: second initial guess
    tolerance: error tolerance

    Returns:
    None
    """

    flag = False
    while not flag and  abs(x1 - x2) >= tolerance and secant.iterations <= 10000:

        # increment the number of iterations
        secant.iterations += 1
        x_m = x2 - ((x2 - x1) * func(coeffs , x2) / (func(coeffs , x2) - func(coeffs , x1)))
        
        if func(coeffs , x_m) == 0:
            print(f'Exact eigenvalue = {x2}')
            flag = True

        x1 = x2
        x2 = x_m

    # if the number of iterations exceeds 10000, print approximate eigenvalue
    if not flag:
        print(f'Approximate eigenvalue = {x2}')


def tridiagonal_mat(mat, n):
    """
    Function to convert a matrix into a tridiagonal matrix

    Parameters:
    mat: matrix to be converted
    n: number of rows/columns in the matrix

    Returns:
    mat: tridiagonal matrix
    """

    for i in range(1 , n):
        for j in range(i+1 , n):
            theta = np.arctan(mat[i-1][j] / mat[i-1][i])
            S = np.identity(n)
            S[i][i] = np.cos(theta)
            S[i][j] = -np.sin(theta)
            S[j][i] = np.sin(theta)
            S[j][j] = np.cos(theta)
            mat = S.T @ mat @ S
    
    return mat


def sturm_sequence(mat, n):
    """
    Function to generate the Sturm sequence of a matrix

    Parameters:
    mat: matrix whose Sturm sequence is to be generated
    n: number of rows/columns in the matrix

    Returns:
    char_polynomial: characteristic polynomial of the matrix
    sturm_sign_changes: list of number of sign changes in the Sturm sequence
    """

    sturm = []
    f0 = [1.0]
    f1 = [1.0 , -mat[0][0]]
    sturm.append(f0)
    sturm.append(f1)

    # generating the Sturm sequence
    for i in range(1, n):
        
        factor = np.array([1, -mat[i][i]], dtype = np.float64)
        temp = [s * factor[0] for s in f1]
        temp.append(0)
        func1 = np.array(temp, dtype = np.float64)
        func2 = [0]
        for s in f1:
            func2.append(s * factor[1])
        
        func2 = np.array(func2, dtype = np.float64)
        f = func1 + func2
        c = mat[i - 1][i]
        
        func3 = [0,0]
        for s in f0:
            func3.append(pow(c, 2) * s)
        func3 = np.array(func3, dtype = np.float64)
        
        f = f - func3
        f0 = f1
        f1 = f.tolist()
        sturm.append(f1)

    # generating the characteristic polynomial
    char_polynomial  = sturm[-1].copy()

    sturm_sign_table = []
    for x in range(-10, 11):
        signs = []
        for k in sturm:
            sum = 0
            for j in range(len(k)):
                sum += k[j] * np.power(x, len(k) - j - 1)

            if sum < 0:
                signs.append(-1)
            elif sum > 0:
                signs.append(+1)
            else:
                signs.append(0)
                
        sturm_sign_table.append(signs)

    # generating the list of number of sign changes
    sturm_sign_changes = []
    for i in sturm_sign_table:
        sign_changes = 0
        for j in range(1, len(i)):
            if i[j] != i[j - 1] and i[j]!= 0:
                sign_changes += 1

        sturm_sign_changes.append(sign_changes)
    
    return char_polynomial, sturm_sign_changes


def print_locations(sign_changes, char_polynomial, tolerance):
    """
    Function to print the locations of eigenvalues

    Parameters:
    sign_changes: list of number of sign changes in the Sturm sequence
    char_polynomial: characteristic polynomial of the matrix
    tolerance: error tolerance

    Returns:
    None
    """

    # finding the locations of eigenvalues
    locations = []
    for i in range(-9, 11):
        if sign_changes[i + 10] != sign_changes[i + 9]:
                locations.append([i - 1 , i])

    # printing the locations of eigenvalues
    for pair in locations:
        exact = False
        for t in range(1):
            if func(char_polynomial, pair[t]) == 0:
                print(f'Exact eigenvalue = {pair[t]}')
                exact = True

        if not exact:
            secant(char_polynomial[::-1], pair[0], pair[1], tolerance)


# Driver code
if __name__ == '__main__':
    
    print("GIVEN'S METHOD FOR EIGENVALUES")
    matrix_A, n = inputMatrix()
    error = float(input("Enter the error tolerance: "))
    print("By default, the interval is taken to be (-10, 10)\n")
    
    secant.iterations = 0
    start = time.time()
    matrix_A = np.array(matrix_A)
    new_mat_A = tridiagonal_mat(matrix_A, n)
    poly, sign__changes = sturm_sequence(new_mat_A, n)
    print_locations(sign__changes, poly, error)
    end = time.time() - start
    print(f'Iterations to achieve the error tolerance = {secant.iterations}')
    print(f'Time taken for execution = {end} seconds')
