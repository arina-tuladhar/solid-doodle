class Solution(object):
    def minimumArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        
        min_row = rows
        max_row = -1
        min_col = cols
        max_col = -1
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    min_row = min(min_row, i)
                    max_row = max(max_row, i)
                    min_col = min(min_col, j)
                    max_col = max(max_col, j)
        
        # All 1s are enclosed between min_row..max_row and min_col..max_col
        height = max_row - min_row + 1
        width = max_col - min_col + 1
        
        return height * width

sol = Solution()
print(sol.minimumArea([[0,1,0],[1,0,1]]))