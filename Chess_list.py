# EMPTY = "-"
# ROOK = "ROOK"

# # board = []
# # for i in range(8):
# #     row = [EMPTY for i in range(8)]
# #     board.append(row)
# board = [[EMPTY for i in range(8)]for j in range(8)]

# board[0][0] = ROOK
# board[0][7] = ROOK
# board[7][0] = ROOK
# board[7][7] = ROOK

# print(board)
# -------------------------------------------

EMPTY = "-"
KNIGHT = "KNIGHT"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][1] = KNIGHT
board[0][6] = KNIGHT
board[7][1] = KNIGHT
board[7][6] = KNIGHT

board[4][2] = KNIGHT
print(board)
