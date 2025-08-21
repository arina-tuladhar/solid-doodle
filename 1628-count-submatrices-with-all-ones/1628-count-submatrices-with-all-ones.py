class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        
        # Step 1: Build up histogram heights for each column
        for i in range(1, m):
            for j in range(n):
                if mat[i][j] == 1:
                    mat[i][j] += mat[i - 1][j]

        total = 0

        # Step 2: For each row, count submatrices ending at each cell
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    continue
                min_height = mat[i][j]
                for k in range(j, -1, -1):
                    if mat[i][k] == 0:
                        break
                    min_height = min(min_height, mat[i][k])
                    total += min_height  # Count rectangles ending at (i, j) with left edge at column k
        return total

sol = Solution()

mat = [[1, 0, 1], [1, 1, 0], [1, 1, 0]]
print(sol.numSubmat(mat))
        