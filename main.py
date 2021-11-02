

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