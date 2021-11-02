

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
    
    pos = {
        "x": 2,
        "y": 0
    }
    num = 3
    
    result = valid(board, num, pos)
    print(result)


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

# check number validity on given x,y position in board
def valid(b, num, pos):
    #check validity in row
    for i in range(len(b[pos["y"]])):
        if b[pos["y"]][i] == num and i != pos["x"]:
            return False
    
    # check validity in column
    for i in range(len(b)):
        if b[i][pos["x"]] == num and i != pos["y"]:
            return False
    
    # check validity in box
    box = {
        "x": pos["x"] // 3,
        "y": pos["y"] // 3
    }
    
    for i in range(box["y"] * 3 , box["y"] * 3 + 3):
        for j in range(box["x"] * 3 , box["x"] * 3 + 3):
            if b[i][j] == num and (i != pos["x"] or j != pos["y"]):
                return False
    
    return True


if __name__ == "__main__":
    main()