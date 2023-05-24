rows, cols = (6, 5)
board = [[0 for i in range(cols)] for j in range(rows)]
board_string_1 = 'rkn.r.p.....P..PP.PPB.K..'


def make_board(board_string):
  board[0] = []
  
  for i in range(1,6):
    board[i][0] = []
    for j in range(len(board[i])):
      if board_string[0] == '.':
        board[i][j] = None
        board_string = board_string.replace(board_string[0], '', 1)
      else:
        board[i][j] = board_string[0]
        board_string = board_string.replace(board_string[0], '', 1)
  return board


board2 = make_board(board_string_1)

for i in range(len(board2)):
  board2[i].insert(0,0)

# print(board2)


def get_piece(board, col, row):
  if board[-row][col] == None:
    return None
  else:
    return board[-row][col] 


def get_legal_moves(board, col, row):
  piece = get_piece(board, col, row)
  moves = []

        
  if piece == "p":
    nxt_row = row - 1
    for i in range(len(board[nxt_row])):
      if board[nxt_row][i] == None:
        if i == col:
          moves.append([i, nxt_row])
          if get_piece(board, col, nxt_row - 1) == None:
            moves.append((col, nxt_row - 1))
          else:
            pass
      else:
        if isinstance(board[nxt_row][i], str) == True:
          if ord(board[nxt_row][i]) == 80:
            if i == col + 1 or i == col - 1:
              moves.append((i, nxt_row))
        else:
          pass

    return moves

  elif piece == "P":
    nxt_row = row + 1
    for i in range(len(board[-nxt_row])):
      if board[-nxt_row][i] == None:
        if i == col:
          moves.append([i, nxt_row])
          if get_piece(board, col, -nxt_row + 1) == None:
            moves.append((col, nxt_row + 1))
          else:
            pass
      else:
        if isinstance(board[-nxt_row][i], str) == True:
          if board[-nxt_row][i].isupper() == False:
            if i == col + 1 or i == col - 1:
              moves.append((i, nxt_row))
        else:
          pass

    return moves
  else:
    return []


print(get_legal_moves(board2, 5,2))


