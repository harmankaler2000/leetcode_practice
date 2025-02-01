class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, len(board)):
            count_map = Counter(board[i])
            # delete the . entry
            for key in count_map.keys():
                if key != "." and count_map[key] > 1:
                    return False
        
        # check for columns
        for i in range(0, len(board)):
            column = []
            for j in range(0, len(board)):
                column.append(board[j][i])
            count_map = Counter(column)
            # delete the . entry
            for key in count_map.keys():
                if key != "." and count_map[key] > 1:
                    return False
        i = 0
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
