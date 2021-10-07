class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0
        ways = [[0 for col in range(len(obstacleGrid[0]) + 1)]
                for row in range(len(obstacleGrid) + 1)]
        ways[1][1] = 1

        for row in range(1, len(ways)):
            for col in range(1, len(ways[row])):
                if obstacleGrid[row - 1][col - 1] == 1:
                    continue
                # right
                current = ways[row][col]
                if col + 1 < len(ways[row]):
                    if obstacleGrid[row - 1][col] == 0:
                        ways[row][col + 1] += current
                # down
                if row + 1 < len(ways):
                    if obstacleGrid[row][col - 1] == 0:
                        ways[row + 1][col] += current
        return ways[-1][-1]