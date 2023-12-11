# find the next part of the pipe
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
    return []


# lists are not hashable so convert to string
def stringify(coord_list):
    return str(coord_list[0]) + ',' + str(coord_list[1])


# replace non loop characters with I for inside or O for outside
def resolve_line(curr_line):
    is_inside = False
    resolved_line = ''
    section_start = ''
    for curr_char in curr_line:
        # replace non loop characters
        if curr_char == '.':
            resolved_line += ('I' if is_inside else 'O')
        # if crossing the loop switch inside/outside
        else:
            resolved_line += curr_char
            # vertical pipes are always a crossing
            if curr_char == '|' or curr_char == 'S':
                is_inside = not is_inside
            # when starting a horizontal section keep track as a crossing may occur later
            elif curr_char == 'L' or curr_char == 'F':
                section_start = curr_char
            # if the end of a horizontal section goes in a different direction to the start then it's a crossing
            elif curr_char == '7' or curr_char == 'J':
                if (section_start in up) != (curr_char in up):
                    is_inside = not is_inside
                section_start = ''
    return resolved_line


grid = [line.strip() for line in open('input.txt', 'r').readlines()]

# find the start
start = []
for y in range(len(grid)):
    s_ind = grid[y].find('S')
    if s_ind >= 0:
        start = [y, s_ind]
        break

# used for directions
right = 'F-L'
left = '7-J'
down = '7|F'
up = 'J|L'

# work out where the start connects to
curr_pipe = []
if grid[start[0]][start[1] - 1] in right:
    curr_pipe = [start[0], start[1] - 1]
elif grid[start[0]][start[1] + 1] in left:
    curr_pipe = [start[0], start[1] + 1]
elif grid[start[0] - 1][start[1]] in down:
    curr_pipe = [start[0] - 1, start[1]]
elif grid[start[0] + 1][start[1]] in up:
    curr_pipe = [start[0] + 1, start[1]]

# traverse the loop from the start
the_loop = set()
the_loop.add(stringify(start))
prev_pipe = start
while curr_pipe != start:
    the_loop.add(stringify(curr_pipe))
    next_pipe = find_next_coords(curr_pipe, prev_pipe)
    prev_pipe = curr_pipe
    curr_pipe = next_pipe

# remove any non loop pipes
loop_grid = []
for y in range(len(grid)):
    grid_line = ''
    for x in range(len(grid[y])):
        if stringify([y, x]) in the_loop:
            grid_line += grid[y][x]
        else:
            grid_line += '.'
    loop_grid.append(grid_line)
    print(grid_line)

print('\n')

# resolve each line and sum the number of inside locations
total = 0
for loop_grid_line in loop_grid:
    res_line = resolve_line(loop_grid_line)
    total += res_line.count('I')
    print(res_line)

print(total)
