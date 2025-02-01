class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose the matrix
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # reflection
        for i in range(n):
            # we only want to parse one half and replace it with the other
            for j in range(n//2):
                matrix[i][n-j-1], matrix[i][j] = matrix[i][j], matrix[i][n-j-1]
