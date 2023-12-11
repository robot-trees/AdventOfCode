def find_next_coords(curr_coords, prev_coords):
    map_symbol = grid[curr_coords[0]][curr_coords[1]]
    diffs = []
    if map_symbol in up:
        diffs.append([-1, 0])
    if map_symbol in down:
        diffs.append([1, 0])
    if map_symbol in left:
        diffs.append([0, -1])
    if map_symbol in right:
        diffs.append([0, 1])
    for diff in diffs:
        next_coords = [curr_coords[0] + diff[0], curr_coords[1] + diff[1]]
        if next_coords != prev_coords:
            return next_coords
    return curr_coords


def move(curr_pos, next_step):
    return [curr_pos[0] + next_step[0], curr_pos[1] + next_step[1]]


right = 'F-L'
left = '7-J'
down = '7|F'
up = 'J|L'

grid = [line.strip() for line in open('input.txt', 'r').readlines()]

start = []
for y in range(len(grid)):
    s_ind = grid[y].find('S')
    if s_ind >= 0:
        start = [y, s_ind]
        break

from_start = []
if grid[start[0]][start[1] - 1] in right:
    from_start.append([start[0], start[1] - 1])
if grid[start[0]][start[1] + 1] in left:
    from_start.append([start[0], start[1] + 1])
if grid[start[0] - 1][start[1]] in down:
    from_start.append([start[0] - 1, start[1]])
if grid[start[0] + 1][start[1]] in up:
    from_start.append([start[0] + 1, start[1]])

curr_left, curr_right = from_start
prev_left = start
prev_right = start
distance = 1
while curr_left != curr_right:
    print(left + right)
    next_left = find_next_coords(curr_left, prev_left)
    prev_left = curr_left
    curr_left = next_left
    next_right = find_next_coords(curr_right, prev_right)
    prev_right = curr_right
    curr_right = next_right
    distance += 1

print(distance)

