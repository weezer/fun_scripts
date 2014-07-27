'''
Created on Jul 26, 2014

@author: Weezer
'''
from random import randint
def gen_board(height,length,mines_to_use):
    board = [[0 for i in range(length)] for j in range(height)]

    mines = []
    #Add mines
    mines_laid = 0
    while mines_laid < mines_to_use:
        y = randint(0,height-1)
        x = randint(0,length-1)

        if board[y][x] != '*':
            board[y][x] = '*'
            mines.append([y,x])
            mines_laid += 1

    for mine in mines:
        print mine
        for i in range(-1,2):
            for j in range(-1,2):
                if (mine[0] + i )!= -1 and (mine[1] + j) != -1:
                    try:
                        if board[mine[0] + i][mine[1] + j] != '*':
                            board[mine[0] + i][mine[1] + j] += 1
                    except:
                        pass

    num_mine = 0
    for i in range(height):
        for j in range(length):
            board[i][j] = str(board[i][j])
            if board[i][j] == '*':
                num_mine += 1
    print num_mine

    return board

if __name__ == '__main__':
    for i in gen_board(7,7,15):
        print i