import pygame, sys, time
from pygame.locals import *

pygame.init()
GAMEWINDOW = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Chess')

white = (255, 255, 255)
board = [['br1', 'bh1', 'bb1', 'bq ', 'bk ', 'bb2', 'bh2', 'br2'],
         ['bp1', 'bp2', 'bp3', 'bp4', 'bp5', 'bp6', 'bp7', 'bp8'],
         ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
         ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
         ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
         ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
         ['wp8', 'wp7', 'wp6', 'wp5', 'wp4', 'wp3', 'wp2', 'wp1'],
         ['wr2', 'wh2', 'wb2', 'wq ', 'wk ', 'wb1', 'wh1', 'wr1']]

boardImg = pygame.image.load('/Users/jayeshmuley/Desktop/Codes/Chess_Game/lib/imgs/board.png')
coin_imgs = {}
coin_imgs['br1'] = pygame.image.load('/Users/jayeshmuley/Desktop/Codes/Chess_Game/lib/imgs/black_rook.png')
coin_imgs['bh1'] = pygame.image.load('/Users/jayeshmuley/Desktop/Codes/Chess_Game/lib/imgs/black_knight.png')
coin_imgs['bb1'] = pygame.image.load('/Users/jayeshmuley/Desktop/Codes/Chess_Game/lib/imgs/black_bishop.png')
coin_imgs['bq '] = pygame.image.load('/Users/jayeshmuley/Desktop/Codes/Chess_Game/lib/imgs/black_queen.png')
coin_imgs['bk '] = pygame.image.load('/Users/jayeshmuley/Desktop/Codes/Chess_Game/lib/imgs/black_king.png')
coin_imgs['bb2'] = pygame.image.load('/Users/jayeshmuley/Desktop/Codes/Chess_Game/lib/imgs/black_bishop.png')
coin_imgs['bh2'] = pygame.image.load('/Users/jayeshmuley/Desktop/Codes/Chess_Game/lib/imgs/black_knight.png')
coin_imgs['br2'] = pygame.image.load('/Users/jayeshmuley/Desktop/Codes/Chess_Game/lib/imgs/black_rook.png')
for i in range(1, 9):
    coin_imgs['bp' + str(i)] = pygame.image.load('/Users/jayeshmuley/Desktop/Codes/Chess_Game/lib/imgs/black_pawn.png')

coin_imgs['wr1'] = pygame.image.load('/Users/jayeshmuley/Desktop/Codes/Chess_Game/lib/imgs/white_rook.png')
coin_imgs['wh1'] = pygame.image.load('/Users/jayeshmuley/Desktop/Codes/Chess_Game/lib/imgs/white_knight.png')
coin_imgs['wb1'] = pygame.image.load('/Users/jayeshmuley/Desktop/Codes/Chess_Game/lib/imgs/white_bishop.png')
coin_imgs['wq '] = pygame.image.load('/Users/jayeshmuley/Desktop/Codes/Chess_Game/lib/imgs/white_queen.png')
coin_imgs['wk '] = pygame.image.load('/Users/jayeshmuley/Desktop/Codes/Chess_Game/lib/imgs/white_king.png')
coin_imgs['wb2'] = pygame.image.load('/Users/jayeshmuley/Desktop/Codes/Chess_Game/lib/imgs/white_bishop.png')
coin_imgs['wh2'] = pygame.image.load('/Users/jayeshmuley/Desktop/Codes/Chess_Game/lib/imgs/white_knight.png')
coin_imgs['wr2'] = pygame.image.load('/Users/jayeshmuley/Desktop/Codes/Chess_Game/lib/imgs/white_rook.png')
for i in range(1, 9):
    coin_imgs['wp' + str(i)] = pygame.image.load('/Users/jayeshmuley/Desktop/Codes/Chess_Game/lib/imgs/white_pawn.png')

coin_imgs['   '] = pygame.image.load('/Users/jayeshmuley/Desktop/Codes/Chess_Game/lib/imgs/blank.png')


def print_board(board, last_move):
    GAMEWINDOW.blit(boardImg, (0, 0))
    if len(last_move):
        x1 = last_move[0][1] * 100
        y1 = last_move[0][0] * 100
        x2 = last_move[1][1] * 100
        y2 = last_move[1][0] * 100
        pygame.draw.rect(GAMEWINDOW, [0, 0, 255], [x1 + 10, y1 + 10, 80, 80], 3)
        pygame.draw.rect(GAMEWINDOW, [255, 0, 0], [x2 + 10, y2 + 10, 80, 80], 3)
    x = 20
    y = 20
    for i in range(8):
        for j in range(8):
            GAMEWINDOW.blit(coin_imgs[board[i][j]], (x, y))
            x += 100
        x = 20
        y += 100


def return_valid_moves(board, piece):
    valid_moves = []

    x = [x for x in board if piece in x]
    if len(x):
        x = x[0]
    else:
        return []
    x, y = board.index(x), x.index(piece)

    if board[x][y][0] == 'w':
        if board[x][y][1] == 'p':
            if 0 <= x - 1 <= 7 and 0 <= y <= 7:
                if board[x - 1][y] == '   ':
                    valid_moves.append((x - 1, y))
            if 0 <= x - 2 <= 7 and 0 <= y <= 7 and board[x - 1][y] == '   ':
                if x == 6 and board[x - 2][y] == '   ':
                    valid_moves.append((x - 2, y))
            if 0 <= x - 1 <= 7 and 0 <= y - 1 <= 7:
                if board[x - 1][y - 1] != '   ' and board[x - 1][y - 1][0] == 'b':
                    valid_moves.append((x - 1, y - 1))
            if 0 <= x - 1 <= 7 and 0 <= y + 1 <= 7:
                if board[x - 1][y + 1] != '   ' and board[x - 1][y + 1][0] == 'b':
                    valid_moves.append((x - 1, y + 1))
        # promotion left
        elif board[x][y][1] == 'h':
            p = [(-1, 2), (-1, -2), (1, 2), (1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
            for i in p:
                x1 = x + i[0]
                y1 = y + i[1]
                if 0 <= x1 <= 7 and 0 <= y1 <= 7:
                    if board[x1][y1][0] != 'w':
                        valid_moves.append((x1, y1))

        elif board[x][y][1] == 'k':
            p = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for i in p:
                x1 = x + i[0]
                y1 = y + i[1]
                if 0 <= x1 <= 7 and 0 <= y1 <= 7:
                    if board[x1][y1][0] != 'w':
                        valid_moves.append((x1, y1))

        elif board[x][y][1] == 'r':
            check_valid_in_four_directions_rook(x, y, 'x', '+', valid_moves)
            check_valid_in_four_directions_rook(x, y, 'x', '-', valid_moves)
            check_valid_in_four_directions_rook(x, y, 'y', '+', valid_moves)
            check_valid_in_four_directions_rook(x, y, 'y', '-', valid_moves)

        elif board[x][y][1] == 'b':
            check_valid_in_four_directions_bishop(x, y, '+', '+', valid_moves)
            check_valid_in_four_directions_bishop(x, y, '+', '-', valid_moves)
            check_valid_in_four_directions_bishop(x, y, '-', '+', valid_moves)
            check_valid_in_four_directions_bishop(x, y, '-', '-', valid_moves)

        elif board[x][y][1] == 'q':
            check_valid_in_four_directions_rook(x, y, 'x', '+', valid_moves)
            check_valid_in_four_directions_rook(x, y, 'x', '-', valid_moves)
            check_valid_in_four_directions_rook(x, y, 'y', '+', valid_moves)
            check_valid_in_four_directions_rook(x, y, 'y', '-', valid_moves)
            check_valid_in_four_directions_bishop(x, y, '+', '+', valid_moves)
            check_valid_in_four_directions_bishop(x, y, '+', '-', valid_moves)
            check_valid_in_four_directions_bishop(x, y, '-', '+', valid_moves)
            check_valid_in_four_directions_bishop(x, y, '-', '-', valid_moves)

    elif board[x][y][0] == 'b':

        if board[x][y][1] == 'p':
            if 0 <= x + 1 <= 7 and 0 <= y <= 7:
                if board[x + 1][y] == '   ':
                    valid_moves.append((x + 1, y))
            if 0 <= x + 2 <= 7 and 0 <= y <= 7:
                if x == 1 and board[x + 2][y] == '   ' and board[x + 1][y] == '   ':
                    valid_moves.append((x + 2, y))
            if 0 <= x + 1 <= 7 and 0 <= y - 1 <= 7:
                if board[x + 1][y - 1] != '   ' and board[x + 1][y - 1][0] == 'w':
                    valid_moves.append((x + 1, y - 1))
            if 0 <= x + 1 <= 7 and 0 <= y + 1 <= 7:
                if board[x + 1][y + 1] != '   ' and board[x + 1][y + 1][0] == 'w':
                    valid_moves.append((x + 1, y + 1))
        # promotion left
        elif board[x][y][1] == 'h':
            p = [(-1, 2), (-1, -2), (1, 2), (1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
            for i in p:
                x1 = x + i[0]
                y1 = y + i[1]
                if 0 <= x1 <= 7 and 0 <= y1 <= 7:
                    if board[x1][y1][0] != 'b':
                        valid_moves.append((x1, y1))

        elif board[x][y][1] == 'k':
            p = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for i in p:
                x1 = x + i[0]
                y1 = y + i[1]
                if 0 <= x1 <= 7 and 0 <= y1 <= 7:
                    if board[x1][y1][0] != 'b':
                        valid_moves.append((x1, y1))

        elif board[x][y][1] == 'r':
            check_valid_in_four_directions_rook(x, y, 'x', '+', valid_moves)
            check_valid_in_four_directions_rook(x, y, 'x', '-', valid_moves)
            check_valid_in_four_directions_rook(x, y, 'y', '+', valid_moves)
            check_valid_in_four_directions_rook(x, y, 'y', '-', valid_moves)

        elif board[x][y][1] == 'b':
            check_valid_in_four_directions_bishop(x, y, '+', '+', valid_moves)
            check_valid_in_four_directions_bishop(x, y, '+', '-', valid_moves)
            check_valid_in_four_directions_bishop(x, y, '-', '+', valid_moves)
            check_valid_in_four_directions_bishop(x, y, '-', '-', valid_moves)

        elif board[x][y][1] == 'q':
            check_valid_in_four_directions_rook(x, y, 'x', '+', valid_moves)
            check_valid_in_four_directions_rook(x, y, 'x', '-', valid_moves)
            check_valid_in_four_directions_rook(x, y, 'y', '+', valid_moves)
            check_valid_in_four_directions_rook(x, y, 'y', '-', valid_moves)
            check_valid_in_four_directions_bishop(x, y, '+', '+', valid_moves)
            check_valid_in_four_directions_bishop(x, y, '+', '-', valid_moves)
            check_valid_in_four_directions_bishop(x, y, '-', '+', valid_moves)
            check_valid_in_four_directions_bishop(x, y, '-', '-', valid_moves)

    return valid_moves


def check_valid_in_four_directions_rook(x, y, var, sym, valid_moves):
    x1 = y1 = 0
    if board[x][y][0] == 'w':
        a = 'w'
        b = 'b'
    else:
        a = 'b'
        b = 'w'
    for i in range(1, 8):
        if var == 'x':
            y1 = y
            if sym == '+':
                x1 = x + i
            else:
                x1 = x - i
        else:
            x1 = x
            if sym == '+':
                y1 = y + i
            else:
                y1 = y - i

        if 0 <= x1 <= 7 and 0 <= y1 <= 7:
            if board[x1][y1][0] == a:
                break
            if board[x1][y1][0] == b:
                valid_moves.append((x1, y1))
                break
            else:
                valid_moves.append((x1, y1))


def check_valid_in_four_directions_bishop(x1, y1, sym1, sym2, valid_moves):
    if board[x1][y1][0] == 'w':
        a = 'w'
        b = 'b'
    else:
        a = 'b'
        b = 'w'

    for i in range(1, 8):
        if sym1 == '+':
            if sym2 == '+':
                x1 += 1
                y1 += 1
            else:
                x1 += 1
                y1 -= 1
        else:
            if sym2 == '+':
                x1 -= 1
                y1 += 1
            else:
                x1 -= 1
                y1 -= 1

        if 0 <= x1 <= 7 and 0 <= y1 <= 7:
            if board[x1][y1][0] == a:
                break
            if board[x1][y1][0] == b:
                valid_moves.append((x1, y1))
                break
            else:
                valid_moves.append((x1, y1))


def check_king_in_check(board, piece):
    x = [x for x in board if piece in x][0]
    x, y = board.index(x), x.index(piece)

    if piece[0] == 'w':
        all_piece_list = ['br1', 'bh1', 'bb1', 'bq ', 'bk ', 'bb2', 'bh2', 'br2', 'bp1', 'bp2', 'bp3', 'bp4', 'bp5',
                          'bp6', 'bp7', 'bp8']
    else:
        all_piece_list = ['wr2', 'wh2', 'wb2', 'wq ', 'wk ', 'wb1', 'wh1', 'wr1', 'wp8', 'wp7', 'wp6', 'wp5', 'wp4',
                          'wp3', 'wp2', 'wp1']
    for i in all_piece_list:
        l = return_valid_moves(board, i)
        if (x, y) in l:
            return 1
    return 0


def copy_list(orig):
    dup = []
    for i in range(len(orig)):
        temp = []
        for j in range(len(orig[0])):
            temp.append(orig[i][j])
        dup.append(temp)
    return dup


def print_valid_moves(valid_moves):
    for pos in valid_moves:
        s = pygame.Surface((100, 100))
        s.set_alpha(40)
        s.fill((0, 0, 255))
        GAMEWINDOW.blit(s, ((pos[1] * 100, pos[0] * 100)))
        pygame.draw.rect(GAMEWINDOW, [0, 0, 255], [pos[1] * 100, pos[0] * 100, 100, 100], 3)


def check_pawn_promotion(board, x, y):
    if board[x][y][:-1] == 'wp' and x == 0:
        print('white promotion')
    elif board[x][y][:-1] == 'bp' and x == 7:
        print('black promotion')


current_move = 'w'
waiting = False
undo_board = copy_list(board)
obj = pygame.font.Font('freesansbold.ttf', 25)
last_move = []
while True:
    print_board(board, last_move)
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        xpos, ypos = event.pos
        x1 = ypos // 100
        y1 = xpos // 100

        if board[x1][y1][0] == current_move:
            move = (x1, y1)
            waiting = True

        if waiting:
            if board[x1][y1][0] == current_move:
                move = (x1, y1)
            elif (x1, y1) in return_valid_moves(board, board[move[0]][move[1]]):
                undo_board = copy_list(board)
                board[x1][y1] = board[move[0]][move[1]]
                board[move[0]][move[1]] = '   '
                waiting = False
                value = check_king_in_check(board, current_move + 'k ')
                last_move = []
                last_move.append(move)
                last_move.append((x1, y1))

                if value:
                    surf = obj.render('Invalid move!!!', True, (0, 0, 0))
                    last_move.clear()
                    GAMEWINDOW.blit(surf, (300, 300))
                    pygame.display.update()
                    time.sleep(1)
                    board = copy_list(undo_board)
                else:
                    if current_move == 'w':
                        current_move = 'b'
                    else:
                        current_move = 'w'

                check_pawn_promotion(board, x1, y1)


            else:
                waiting = False

    if waiting:
        print_valid_moves(return_valid_moves(board, board[move[0]][move[1]]))

    value = check_king_in_check(board, current_move + 'k ')
    if value:
        surf = obj.render('You are under check!!!', True, (0, 0, 0))
        GAMEWINDOW.blit(surf, (300, 300))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_u] and len(last_move):
        last_move.clear()
        board = copy_list(undo_board)
        if current_move == 'w':
            current_move = 'b'
        else:
            current_move = 'w'

    pygame.display.update()