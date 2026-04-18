def sudoku(L, x, y):
    if y==9:
        return sudoku(L, x+1, 0)
    if x==9:
        return True
    if L[x][y] != 0:
        return sudoku(L, x, y+1)

    S = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    for i in range(9):
        if L[x][i] in S:
            S.remove(L[x][i])
    for i in range(9):
        if L[i][y] in S:
            S.remove(L[i][y])
    for i in range(3):
        for j in range(3):
            if L[x-x%3+i][y-y%3+j] in S:
                S.remove(L[x-x%3+i][y-y%3+j])
    
    S = list(S)
    for number in S:
        L[x][y]=number
        if sudoku(L, x, y+1) == True:
            return True
    
    L[x][y]=0
    return False

def print_board(L):
    for i in range(9):
        print(L[i])



sudoku_puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
sudoku(sudoku_puzzle,0,0)

print_board(sudoku_puzzle)
