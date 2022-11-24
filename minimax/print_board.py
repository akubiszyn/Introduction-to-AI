def print_board(board):
    for j in range(3):
        for i in range(3):
            match board[j][i]:
                case 1:
                    character = "X"
                case -1:
                    character = "O"
                case 0:
                    character = ' '
            print(" " + character + " ", end = '')
            if i < 2:
                print('|', end='')
        if j < 2:
            print(end='\n'"-----------")
            print()
    print()
    print()
    print()