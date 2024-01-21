# import necessary libraries
import warnings

# ignore warnings
warnings.filterwarnings('ignore')

"""
Sample Case 1
2x + y - z = 8
-3x - 1y + 2z = -11
-2x + y + 2z = -3

x = 2, y = 3, z = -1

Sample Case 2
2x + 5y = 16
3x + y = 11

x = 3, y = 2

Sample Case 3
x + 2z = 4
-2x + 3y + 2z = 9
3x - 5y + 5z = 11

x = -2.074, y = -0.407, z = 3.037
"""

def inputMatrix():
    """
    Function to take input of augmented matrix from user

    Returns:
    mat: augmented matrix
    M: number of variables
    """

    # take input of number of variables
    try:
        M = int(input("Enter the number of variables: "))
    except ValueError:
        raise Exception(f'Invalid input - number of variables should be positive integers')
    if M < 1:
        raise Exception(f'Invalid input - number of variables should be positive integers')

    mat = []
    print("Enter the elements of the augmented-matrix as space-separated floating points")
    
    # take input of augmented matrix
    try:
        for i in range(M):
            if i == 0:
                row = input(f'Enter elements of {i+1}st equation: ').split()
                row = [float(x) for x in row]
                if len(row) != M+1:
                    raise Exception(f'Invalid input - Each row should contain {M+1} element(s), input has {len(row)} element(s)')
            elif i == 1:
                row = input(f'Enter elements of {i+1}nd equation: ').split()
                row = [float(x) for x in row]
                if len(row) != M+1:
                    raise Exception(f'Invalid input - Each row should contain {M+1} element(s), input has {len(row)} element(s)')
            elif i == 2:
                row = input(f'Enter elements of {i+1}rd equation: ').split()
                row = [float(x) for x in row]
                if len(row) != M+1:
                    raise Exception(f'Invalid input - Each row should contain {M+1} element(s), input has {len(row)} element(s)')
            else:
                row = input(f'Enter elements of {i+1}th equation: ').split()
                row = [float(x) for x in row]
                if len(row) != M+1:
                    raise Exception(f'Invalid input - Each row should contain {M+1} element(s), input has {len(row)} element(s)')
            
            mat.append(row)

    # raise exception if input is invalid
    except ValueError:
        raise Exception(f'Invalid input - Elements of a matrix should be floating point numbers')

    print("Initial Matrix")
    print('[', end='')
    for i in range(len(mat) - 1):
        print(str(mat[i]) + ',', end='\n ')
    print(str(mat[-1]) + ']')
    
    return mat, M, M+1


def gElimination(mat, m, n):
    """
    Function to perform Gaussian Elimination on augmented matrix

    Parameters:
    mat: augmented matrix
    m: number of variables
    n: number of columns

    Returns:
    mat: augmented matrix after Gaussian Elimination
    """

    try:
        R = 0
        C = 0
        while R < m and C < n:
            col_vals = []
            for i in range(R, m):
                col_vals.append(mat[i][C])
            i_max = col_vals.index(max(col_vals)) + R
            if mat[i_max][C] == 0:
                C += 1
            else:
                mat[R], mat[i_max] = mat[i_max], mat[R]
                for i in range(R + 1, m):
                    pivot_div = mat[i][C] / mat[R][C]
                    mat[i][C] = 0
                    for j in range(C + 1, n):
                        mat[i][j] = mat[i][j] - pivot_div * mat[R][j]
                R += 1
                C += 1

    # raise exception if input is invalid
    except:
        raise Exception(f'Invalid Matrix Input - Error while calculating')
    
    for i in range(m):
        for j in range(n):
            mat[i][j] = round(mat[i][j], 3)

    return mat


def back_substitute(mat):
    """
    Function to perform back substitution on augmented matrix

    Parameters:
    mat: augmented matrix

    Returns:
    0: if no solution
    1: if unique solution
    2: if infinite solutions
    """
    
    # copy the augmented matrix
    A = mat.copy()
    B = []
    for i in range(len(mat)):
        B.append(A[i].pop())
    
    n = len(A)
    solutions = [] * n
    zeros_A = A[-1].count(0)
    zero_B = 1 if B[-1] == 0 else 0
    
    # check for solutions
    if zeros_A + zero_B == n + 1:
        return 2    # infinite solutions
    elif zeros_A + zero_B == n:
        return 0    # no solution
    else:
        return 1    # unique solution


# Driver Code
if __name__ == '__main__':

    print("GAUSSIAN ELIMINATION FOR SOLVING LINEAR EQUATIONS")
    A, M, N = inputMatrix()
    final_A = gElimination(A, M, N)

    print("Matrix after Gaussian Elimination")
    print('[', end='')
    for i in range(len(final_A) - 1):
        print(str(final_A[i]) + ',', end='\n ')
    print(str(final_A[-1]) + ']')
    
    res = back_substitute(final_A)
    
    if res == 0:
        print("Given system of linear equations has NO solutions")
    elif res == 2:
        print("Given system of linear equations has INFINITE solutions")
    else:
        print("Given system of linear equations has UNIQUE solution")
