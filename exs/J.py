def is_valid(x, y):
    return 0 <= x < 8 and 0 <= y < 8

def J(board, king_start, pawn_start):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    queue = [(king_start[0], king_start[1], 0)] # x, y, steps
    visited = [[False] * 8 for _ in range(8)]
    visited[king_start[0]][king_start[1]] = True

    while queue:
        king_x, king_y, steps = queue.pop(0)
        # Если король съел пешку
        if (king_x, king_y) == pawn_start:
            return steps

        # Движение пешки
        pawn_x, pawn_y = pawn_start
        if pawn_x < 7:
            pawn_start = (pawn_x + 1, pawn_y)

        # Проверить все возмодные перемещения короля
        for dx, dy in directions:
            new_king_x = king_x + dx
            new_king_y = king_y + dy
            if is_valid(new_king_x, new_king_y) and board[new_king_x][new_king_y] == '0' \
                and not visited[new_king_x][new_king_y]:
                new_king_pos = (new_king_x, new_king_y)
                if new_king_pos == pawn_start:
                    return steps + 1
                visited[new_king_x][new_king_y] = True
                queue.append((new_king_x, new_king_y, steps + 1))

        # Пешка дошла до нижней горизонтали
        if pawn_x == 7:
            continue
    return -1

# Чтение доски
board = [input().strip() for _ in range(8)]
king_start = None
pawn_start = None

# Поиск позиций короля и пешки
for i in range(8):
    for j in range(8):
        if board[i][j] == 'K':
            king_start = (i, j)
        elif board[i][j] == 'ч':
            pawn_start = (i, j)

result = J(board, king_start, pawn_start)
print(result)