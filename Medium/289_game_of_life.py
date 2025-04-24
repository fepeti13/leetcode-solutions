class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        0: Dead now, dead in the next generation.
        1: Live now, dead in the next generation.
        2: Dead now, live in the next generation.
        3: Live now, live in the next generation.
        """
        
        n = len(board)
        m = len(board[0])
        dir_x = [1, 1, 1, -1, -1, -1, 0, 0]
        dir_y = [1, -1, 0, 1, -1, 0, 1, -1]

        for i in range(0, n):
            for j in range(0, m):
                live_count = 0
                for k in range(0, 8):
                    new_i = i + dir_x[k]
                    new_j = j + dir_y[k]
                    if(new_i >= 0 and new_j >= 0 and new_i < n and new_j < m and board[new_i][new_j]%2 == 1):
                        live_count += 1
                
                if board[i][j] == 0 and live_count == 3:
                    board[i][j] = 2
                
                if board[i][j] == 1 and (live_count == 2 or live_count == 3):
                        board[i][j] = 3

        for i in range(0, n):
            for j in range(0, m):
                board[i][j] = board[i][j] // 2