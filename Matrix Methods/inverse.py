# import necessary libraries
import warnings

# ignore warnings
warnings.filterwarnings('ignore')


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
        
        return mat, n
    
    # raise exception if input is invalid
    except ValueError:
        raise Exception(f'Invalid input - Elements of a matrix should be floating point numbers')


def eliminate(row1, row2, col, target=0):
    """
    Function to eliminate a variable from a row

    Parameters:
    row1: row from which the variable is to be eliminated
    row2: row in which the variable is to be eliminated
    col: column in which the variable is to be eliminated
    target: value of the variable to be eliminated

    Returns:
    None
    """

    fac = (row2[col] - target) / row1[col]
    for i in range(len(row2)):
        row2[i] -= fac * row1[i]


def gauss(mat, n):
    """
    Function to perform Gauss Elimination

    Parameters:
    mat: augmented matrix
    n: number of rows

    Returns:
    mat: augmented matrix after Gauss Elimination
    """

    try:
        for i in range(n):
            if mat[i][i] == 0:
                for j in range(i+1, n):
                    if mat[i][j] != 0:
                        mat[i], mat[j] = mat[j], mat[i]
                        break

            for j in range(i+1, n):
                eliminate(mat[i], mat[j], i)

        for i in range(n - 1, -1, -1):
            for j in range(i-1, -1, -1):
                eliminate(mat[i], mat[j], i)

        for i in range(n):
            eliminate(mat[i], mat[i], i, target=1)
    
    # raise exception if input is invalid
    except ZeroDivisionError:
        raise Exception(f'Invalid Matrix Input - Matrix not invertible')

    return mat


def inverse(mat, n):
    """
    Function to calculate inverse of a matrix

    Parameters:
    mat: square matrix
    n: number of rows

    Returns:
    res_mat: inverse of the matrix
    """

    temp = [[] for i in mat]
    for i, row in enumerate(mat):
        assert len(row) == len(mat)
        temp[i].extend(row + [0] * i + [1] + [0] * (n-i-1))
    
    # perform Gauss Elimination for inverse
    gauss(temp, n)
    res_mat = []
    
    for i in range(len(temp)):
        res_mat.append(temp[i][len(temp[i]) // 2:])
        
    for i in range(n):
        for j in range(n):
            res_mat[i][j] = round(res_mat[i][j], 3)
    
    return res_mat


 # Driver Code
if __name__ == '__main__':
    
    print("INVERSE OF A SQUARE MATRIX")
    matrix_A, n = inputMatrix()
    inverse_A = inverse(matrix_A, n)
    
    print("Initial Matrix - ")
    print('[', end='')
    for i in range(len(matrix_A) - 1):
        print(str(matrix_A[i]) + ',', end='\n ')
    print(str(matrix_A[-1]) + ']')
    
    print("Inverse Matrix - ")
    print('[', end='')
    for i in range(len(inverse_A) - 1):
        print(str(inverse_A[i]) + ',', end='\n ')
    print(str(inverse_A[-1]) + ']')
