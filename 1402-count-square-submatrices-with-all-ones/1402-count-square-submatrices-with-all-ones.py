class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        m = len(matrix)
        n = len(matrix[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i > 0 and j > 0:
                        # Update cell with size of largest square ending at (i, j)
                        matrix[i][j] = min(
                            matrix[i - 1][j],      # top
                            matrix[i][j - 1],      # left
                            matrix[i - 1][j - 1]   # top-left
                        ) + 1
                    count += matrix[i][j]

        return count

sol = Solution()
matrix = [[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]
print(sol.countSquares(matrix))