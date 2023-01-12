

def solution(m, n, board):
    board = [list(b) for b in board]
    tmp_inter = set([None])
    answer = 0
    while tmp_inter:
        for x in range(m-1):
            for y in range(n-1):
                if board[x][y] == board[x+1][y] == board[x][y+1] == board[x+1][y+1] != None:
                    tmp_inter.update([(x,y), (x+1,y), (x, y+1), (x+1, y+1)])
        # 더 이상 터질 블락 없으면 끝
        if tmp_inter == set([None]):
            break
        else:
            tmp_inter.remove(None)
            for a, b in tmp_inter:
                board[a][b] = None
            answer += len(tmp_inter)
            tmp_inter = set([None])
            # 터진 블락 있으면, 보드 재배열
            board = [[b[i] for b in board if b[i] is not None] for i in range(n)]
            board = [[None] * (m - len(b)) + b for b in board]
            board = [[b[i] for b in board] for i in range(m)]

    return answer
  
# CCBDE
# AAADE
# AAABF
# CCBBF
# 6개 삭제

# ---DE
# ---DE
# CCBBF
# CCBBF
# 8개 삭제

# ----E
# ----E
# ---DF
# ---DF
# 14개 삭제
