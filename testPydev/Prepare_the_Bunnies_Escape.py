maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0,
                                                                                                             0, 0, 0]]
# maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
arr = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1], [0, 1, 0, 1, 1, 1], [0, 0, 0,
                                                                                                            0, 0, 0]]
maze2 = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0,
                                                                                                             0, 0, 0]]

def bfs(maze, start_point):
    import collections
    queue_positions = collections.deque()
    queue_positions.append(start_point)
    len_maze = len(maze[0])
    hei_maze = len(maze)
    step_map = [[0 for i in range(len_maze)] for j in range(hei_maze)]
    step_map[start_point[0]][start_point[1]] = 1
    while queue_positions:
        c_pos = queue_positions.popleft()
        if c_pos[1] == len_maze - 1 and c_pos[0] == hei_maze - 1:
            return step_map
        #go up
        if c_pos[0] > 0 and step_map[c_pos[0] - 1][c_pos[1]] == 0 and maze[c_pos[0] - 1][c_pos[1]] == 0:
            step_map[c_pos[0] - 1][c_pos[1]] = c_pos[2] + 1
            queue_positions.append([c_pos[0] - 1, c_pos[1],c_pos[2] + 1])
        #go down
        if c_pos[0] < hei_maze - 1 and step_map[c_pos[0] + 1][c_pos[1]] == 0 and maze[c_pos[0] + 1][c_pos[1]] == 0:
            step_map[c_pos[0] + 1][c_pos[1]] = c_pos[2] + 1
            queue_positions.append([c_pos[0] + 1, c_pos[1],c_pos[2] + 1])
        #go left
        if c_pos[1] > 0 and step_map[c_pos[0]][c_pos[1] - 1] == 0 and maze[c_pos[0]][c_pos[1] - 1] == 0:
            step_map[c_pos[0]][c_pos[1] - 1] = c_pos[2] + 1
            queue_positions.append([c_pos[0], c_pos[1] - 1, c_pos[2] + 1])
        #go right
        if c_pos[1] < len_maze - 1 and step_map[c_pos[0]][c_pos[1] + 1] == 0 and maze[c_pos[0]][c_pos[1] + 1] == 0:
            step_map[c_pos[0]][c_pos[1] + 1] = c_pos[2] + 1
            queue_positions.append([c_pos[0], c_pos[1] + 1, c_pos[2] + 1])
        print step_map
    return step_map

# print bfs(maze, [0,0,1])

def find_certified_pos(maze, step_map, pos):
    count = 0
    len_maze = len(maze[0])
    hei_maze = len(maze)
    least_step = 1 << 31
    for i, j in [[1,0], [-1,0], [0,1], [0,-1]]:
        i2 = pos[0] + i
        j2 = pos[1] + j
        if i2 < 0 or i2 == hei_maze or j2 < 0 or j2 == len_maze:
            continue
        elif maze[i2][j2] == 0:
            count += 1
            if step_map[i2][j2] > 0:
                least_step = min(step_map[i2][j2], least_step)
    if count >= 2 or (pos[0] == hei_maze - 1 and pos[1] == len_maze - 1):
        return least_step
    else:
        return False

def find_shortest_one_move_path(maze):
    len_maze = len(maze[0])
    hei_maze = len(maze)
    step_map = bfs(maze, [0,0,1])
    print step_map
    best_step = step_map[hei_maze-1][len_maze-1]
    print "best" + str(best_step)
    if best_step == len_maze + hei_maze - 1:
        return best_step
    least_step = 0
    answer_step = 1 << 31
    for i in range(hei_maze):
        for j in range(len_maze):
            if maze[i][j] == 1:
                least_step = find_certified_pos(maze, step_map, [i, j])
            if least_step:
                step = bfs(maze, [i, j, 1])
                if step[hei_maze-1][len_maze-1] != 0:
                    answer_step = min(least_step + step[hei_maze-1][len_maze-1], answer_step)
            if answer_step == hei_maze + len_maze - 1:
                return answer_step
    return answer_step


ts = [
    [[0, 1],
     [0, 1]],

    [[0, 0, 0, 0]],

    [[0, 1, 0, 0]],

    [[1, 0, 0, 0]],

    [[0, 1, 1, 0]],

    [[0, 0, 1, 0],
     [0, 1, 1, 0]],

    [[0, 0, 0],
     [0, 1, 0],
     [0, 0, 0]],

    [[0, 1, 1, 0],
     [0, 0, 0, 1],
     [1, 1, 0, 0],
     [1, 1, 1, 0]],

    [[0, 1, 0, 0, 0],
     [0, 1, 0, 1, 0],
     [0, 1, 0, 1, 0],
     [0, 0, 0, 1, 0]],

    [[0, 1, 0, 0, 1, 0],
     [0, 1, 1, 1, 1, 0],
     [0, 0, 0, 1, 0, 0],
     [0, 1, 1, 1, 1, 0],
     [0, 0, 1, 0, 0, 0],
     [0, 0, 1, 1, 1, 0]],

    [[0, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 1, 0],
     [0, 1, 1, 1, 1, 0]],

    [[0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 1],
     [0, 1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0, 0]]
]
for i in ts:

    print find_shortest_one_move_path(i)

