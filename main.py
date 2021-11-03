

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def main():
    print_board(board)
    print()
    print()
    solve(board)
    print_board(board)

# solve sudoku board using BackTracking Algorithm
def solve(b):
    find = find_empty(b)
    if not find:
        return True
    
    for i in range(1, 10):
        if valid(b, i, find):
            b[find[0]][find[1]] = i
            
            if solve(b):
                return True
            
            b[find[0]][find[1]] = 0
    
    return False

# check number validity on given x,y position in board
def valid(b, num, pos):
    #check validity in row
    for i in range(len(b[pos[0]])):
        if b[pos[0]][i] == num and i != pos[1]:
            return False
    
    # check validity in column
    for i in range(len(b)):
        if b[i][pos[1]] == num and i != pos[0]:
            return False
    
    # check validity in box
    box = {
        "x": pos[1] // 3,
        "y": pos[0] // 3
    }
    
    for i in range(box["y"] * 3 , box["y"] * 3 + 3):
        for j in range(box["x"] * 3 , box["x"] * 3 + 3):
            if b[i][j] == num and (i,j) != pos:
                return False
    
    return True

def find_empty(b):
    for i in range(len(b)):
        for j in range(len(b[i])):
            if b[i][j] == 0:
                return (i, j) # row, column
    
    return None

def print_board(b):
    print()
    for i in range(len(b)):
        if (i % 3 == 0) and (i != 0):
            print("- - - - - - - - - - - -  ")
        
        for j in range(len(b[i])):
            if (j % 3 == 0) and (j != 0):
                print(" | ", end="")
            
            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end="")
    print()

if __name__ == "__main__":
    main()