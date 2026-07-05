class Solution:
    def equalPairs(self, grid):

        n = len(grid)
        count = 0

        for r in range(n):

            row = grid[r]

            for c in range(n):

                col = []

                for i in range(n):
                    col.append(grid[i][c])

                if row == col:
                    count += 1

        return count
        