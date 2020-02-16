# Compute the number of islands given a grid of values. 1 represents land and 0 represents water
# Example:
# 11010
# 01100
# 10001
# 10001
#
# There are 4 islands in the grid


def num_islands(grid):
    count = 0
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 1:
                count += 1
                search_surrounding(grid, i, j)
    return count


def search_surrounding(grid, i, j):
    if i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[0])-1 or grid[i][j] == 0:
        return
    else:
        # ensure that this part of the island is not double counted
        grid[i][j] = 0

        # search the surrounding region for more land
        search_surrounding(grid, i - 1, j)
        search_surrounding(grid, i + 1, j)
        search_surrounding(grid, i, j - 1)
        search_surrounding(grid, i, j + 1)


my_grid = [[1, 1, 0, 1, 0],
           [0, 1, 1, 0, 0],
           [1, 0, 0, 0, 1],
           [1, 0, 0, 0, 1],]
print(num_islands(my_grid))