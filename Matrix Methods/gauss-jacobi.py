# import necessary libraries
import numpy as np
import time

# Set the maximum number of iterations
MAX_ITERS = 1e6


def inputMatrix() -> tuple(list(list(float)), int):
    """
    Takes input of a square matrix from the user.

    Args:
        None

    Returns:
        tuple(list(list(float)), int): A tuple containing the matrix and its size.
    """

    # Input the number of rows in the square matrix and check for validity
    try:
        n = int(input("Enter the number of rows in the square matrix: "))
    except ValueError:
        raise Exception(f'Invalid input: Rows of a square matrix need to be positive integers')
    if n < 1:
        raise Exception(f'Invalid input: Rows of a square matrix need to be positive integers')

    # Input the elements of the square matrix and check for validity
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
            
            # Adding rows to the matrix
            mat.append(row)
        
        return mat, n
    
    # Raise exception if the input is not a floating point number
    except ValueError:
        raise Exception(f'Invalid input - Elements of a matrix should be floating point numbers')


def dominant(A: list(list(float))) -> bool:
    """
    Checks if the given matrix is strictly diagonally dominant.

    Args:
        A (list(list(float))): The matrix to be checked.

    Returns:
        bool: True if the matrix is strictly diagonally dominant, False otherwise.
    """

    # Iterating over the rows of the matrix
    for i, row in enumerate(A):
        LHS = abs(row[i])
        RHS = sum(abs(ele) for ele in row) - abs(row[i])

        # Check for strictly diagonal dominance
        flag = True if LHS >= RHS else False
        if not flag:
            return False

    return True


def gauss_jacobi(X: list(float), A: list(float), B: list(float), tolerance: float) -> list(float):
    """
    Computes the solution of a system of linear equations using Gauss-Jacobi Iterative Method.

    Args:
        X (list(float)): The initial guess matrix.
        A (list(float)): The coefficient matrix.
        B (list(float)): The constant matrix.
        tolerance (float): The error tolerance.
    
    Returns:
        list(float): The solution of the system of linear equations.
    """

    # Converting input parameters to numpy arrays
    X = np.array(X)
    A = np.array(A)
    B = np.array(B)
    
    # Performing Gauss-Jacobi Iterative Method until error tolerance is achieved
    while True:
        gauss_jacobi.iterations += 1
        X_new = np.zeros_like(X)

        for i in range(A.shape[0]):
            s1 = np.dot(A[i, :i], X[:i])
            s2 = np.dot(A[i, i + 1:], X[i + 1:])
            X_new[i] = (B[i] - s1 - s2) / A[i, i]
            if X_new[i] == X_new[i-1]:
              break

        if np.allclose(X, X_new, atol=tolerance, rtol=0.):
            break
        
        if gauss_jacobi.iterations == MAX_ITERS:
            break

        X = X_new
    return X


def print_system(A: list(list(float)), B: list(float)) -> None:
    """
    Print the system of equations of form AX = B in console.

    Args:
        A (list(list(float))): The coefficient matrix.
        B (list(float)): The constant matrix.
    
    Returns:
        None
    """

    # Initializing the variables
    variables = ['x'+str(i+1) for i in range(len(A))]

    # Iterating through every row to fetch linear equations
    for i in range(len(A)):
        string = ''
        string = str(A[i][0]) + '*' + variables[0] + ' '
        
        for idx, coeff in enumerate(A[i]):
            if idx == 0:
                continue
            elif coeff >= 0:
                string += '+ ' + str(coeff) + '*' + variables[idx] + ' '
            elif coeff < 0:
                string += '- '+ str(abs(coeff)) + '*' + variables[idx] + ' '
        
        string += '= ' + str(B[i])
        print(string)


# Driver code
if __name__ == '__main__':
    
    print("GAUSS-JACOBI ITERATIVE METHOD")
    
    # Input the matrix and check for validity
    matrix_A, n = inputMatrix()
    matrix_B = list(map(float, input("Enter the elements of B matrix as space-separated numbers: ").split()))

    if len(matrix_B) != n:
        raise Exception(f'Invalid input: Number of elements in B matrix should be {n}')
    
    if dominant(matrix_A) == False:
        raise Exception(f'Given matrix is not strictly diagonally dominant: Gauss-Jacobi Fails')
    
    # Input the initial guess matrix and error tolerance
    init_mat = list(map(float, input("Initial guess matrix: ").split()))
    error = float(input("Enter the error tolerance: "))
    
    # Timing the execution of the algorithm
    start = time.time()
    gauss_jacobi.iterations = 0
    final_X = gauss_jacobi(init_mat, matrix_A, matrix_B, error)
    end = time.time() - start
    
    # Output the results
    print("\nApproximate solution for the given system of linear equations is: ")
    print_system(matrix_A, matrix_B)
    print("\n")

    for i in range(len(final_X)):
        if i != len(final_X) - 1:
            print(f'x{i+1} = {final_X[i]}', end=',\n')
        else:
            print(f'x{i+1} = {final_X[i]}')

    print(f'Iterations to achieve the error tolerance = {gauss_jacobi.iterations}')
    print(f'Time taken for execution = {end} seconds')
