class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            item_set = set()
            for j in range(9):
                if board[i][j] in item_set:
                    return False
                elif board[i][j] != '.':
                    item_set.add(board[i][j])
        
        # check for columns
        for i in range(9):
            item_set = set()
            for j in range(9):
                if board[j][i] in item_set:
                    return False
                elif board[j][i] != '.':
                    item_set.add(board[j][i])
        # check for 3x3 matrix
        starts = [(0, 0), (0, 3), (0, 6),
                  (3, 0), (3, 3), (3, 6),
                  (6, 0), (6, 3), (6, 6)]

        for i, j in starts:
            s = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    item = board[row][col]
                    if item in s:
                        return False
                    elif item != '.':
                        s.add(item)
        return True
