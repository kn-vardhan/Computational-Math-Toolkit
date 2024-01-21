# import necessary libraries
import numpy as np
import warnings

# ignore warnings
warnings.filterwarnings('ignore')

# set numpy to raise exceptions
np.seterr(all='raise')


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
        raise Exception(f'Invalid input - Rows of a square matrix need to be positive integers')

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
        
        return mat
    
    # raise exception if input is invalid
    except ValueError:
        raise Exception(f'Invalid input - Elements of a matrix should be floating point numbers')


def LU_decompose(A):
    """
    Function to perform LU Decomposition of a square matrix

    Parameters:
    A: square matrix

    Returns:
    L: lower triangular matrix
    U: upper triangular matrix
    """

    # check if the matrix is square
    n = A.shape[0]
    U = A.copy()
    L = np.eye(n, dtype=np.float)

    for i in range(n):
        lu_factor = U[i+1:, i] / U[i, i]
        L[i+1:, i] = lu_factor
        U[i+1:] -= lu_factor[:, np.newaxis] * U[i]

    L = L.tolist()
    U = U.tolist()
    
    for i in range(n):
        for j in range(n):
            L[i][j] = round(L[i][j], 3)
            U[i][j] = round(U[i][j], 3)

    return L, U


# Driver code
if __name__ == '__main__':

    try:
        print("LU DECOMPOSITION OF A SQUARE MATRIX")
        mat = inputMatrix()
        L, U = LU_decompose(np.array(mat))

    except FloatingPointError:
        raise Exception(f'Cannot perform LU Decomposition for the input matrix')
    
    print("Initial Matrix - ")
    print('[', end='')
    for i in range(len(mat) - 1):
        print(str(mat[i]) + ',', end='\n ')
    print(str(mat[-1]) + ']')
    print("L Matrix - ")
    print('[', end='')
    for i in range(len(L) - 1):
        print(str(L[i]) + ',', end='\n ')
    print(str(L[-1]) + ']')
    print("U Matrix - ")
    print('[', end='')
    for i in range(len(U) - 1):
        print(str(U[i]) + ',', end='\n ')
    print(str(U[-1]) + ']')
