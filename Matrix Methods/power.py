# import necessary libraries
import numpy as np
import time

# Set the maximum number of iterations
MAX_ITERS = 1e6


def inputMatrix():
    """
    Function to take input of augmented matrix from user

    Returns:
    mat: augmented matrix
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


def power_method(mat, v, tolerance):
    """
    Function to find the largest eigenvalue of a matrix using power method

    Parameters:
    mat: matrix
    v: initial guess vector
    tolerance: error tolerance

    Returns:
    val: largest eigenvalue of the matrix
    """

    while True:
        # increment the number of iterations
        power_method.iterations += 1
        y = np.dot(mat, v)
        m = max(abs(x) for x in y)
        new_v = [x / m for x in y]

        if np.allclose(y, np.dot(mat, new_v), atol=tolerance, rtol=0.):
            break
        
        if power_method.iterations == MAX_ITERS:
            break
        
        v = new_v

    return max(np.divide(np.dot(mat, new_v), v))


# Driver code
if __name__ == '__main__':
    
    print("POWER ITERATIVE METHOD")
    print("NOTE: Depending on the error tolerance, this method might take time as the rate of convergence is low")
    
    matrix_A, n = inputMatrix()
    init_V = list(map(float, input("Initial guess vector: ").split()))
    error = float(input("Enter the error tolerance: "))
    
    if len(init_V) != n:
        raise Exception(f'Invalid input: Number of elements in vector should be {n}')
    
    start = time.time()
    power_method.iterations = 0
    val = power_method(matrix_A, init_V, error)
    end = time.time() - start
    
    print(f'Approximate largest eigenvalue of matrix A = {val}')
    print(f'Iterations to achieve the error tolerance = {power_method.iterations}')
    print(f'Time taken for execution = {end} seconds')
