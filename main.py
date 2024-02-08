def check_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ' or \
           board[0][i] == board[1][i] == board[2][i] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] != ' ' or \
       board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False

def check_draw(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

list = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def print_board(board):
    print('   #---#---#---#')
    for row in board:
        print('   | ' + ' | '.join(row) + ' |')
        print('   #---#---#---#')

counter = 0
while True:
    print_board(list)
    if counter % 2 == 0:
        print('X turn')
    else:
        print('O turn')

    pos = input('Enter a number from 1 to 9: ')
    pos = int(pos) - 1
    row, col = divmod(pos, 3)

    if 0 <= pos <= 8 and list[row][col] == ' ':
        if counter % 2 == 0:
            list[row][col] = 'X'
        else:
            list[row][col] = 'O'
        counter += 1

        if check_win(list):
            print_board(list)
            if counter % 2 == 0:
                print('O wins!')
            else:
                print('X wins!')
            break

        if check_draw(list):
            print_board(list)
            print("It's a draw!")
            break
    else:
        print('Invalid position or position already taken')