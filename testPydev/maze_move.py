grid = [[0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 2]]


def search(x, y):
    if grid[x][y] == 2:
        return True
    elif grid[x][y] == 1:
        return False
    elif grid[x][y] == 3:
        return False

    grid[x][y] = 3

    if (x > 0 and search(x-1, y)) or (x + 1 < len(grid) and search(x+1, y)) or (y > 0 and search(x, y-1)) or\
                                             (y+1 < len(grid[0]) and search(x, y+1)):
        return True
    return False

print search(0, 0)