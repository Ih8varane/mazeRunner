#wall logic is for coordinates (x, y) north wall is (x, y+1) south wall is (x, y) east wall is (y, x+1) west wall is (y, x)

def create_maze(width: int, height: int) -> dict:
    maze = {"width": width, "height": height, "walls": {"horizontal": set(), "vertical": set()}}
    add_horizontal_outer_walls(maze, width, height)
    add_vertical_outer_walls(maze, width, height)
    return maze
#need to add outer walls

def add_horizontal_outer_walls(maze: dict, width: int, height: int) -> dict:
    for box in range(width):
        maze = add_horizontal_wall(maze, box, 0)  # South outer wall
        maze = add_horizontal_wall(maze, box, height)  # North outer wall
    return maze

def add_vertical_outer_walls(maze: dict, width: int, height: int) -> dict:
    for box in range(height):
        maze = add_vertical_wall(maze, 0, box)  # west outer wall
        maze = add_vertical_wall(maze, width, box)  # east outer wall
    return maze

def add_horizontal_wall(maze: dict, x_coordinate: int, horizontal_line: int) -> dict:
    horizontal_wall = (x_coordinate, horizontal_line)
    maze["walls"]["horizontal"].add(horizontal_wall)
    return maze

def add_vertical_wall(maze: dict, y_coordinate: int, vertical_line: int) -> dict:
    vertical_wall = (y_coordinate, vertical_line)
    maze["walls"]["vertical"].add(vertical_wall)
    return maze

def get_dimensions(maze: dict) -> tuple[int, int]:
    return maze["width"], maze["height"]

def get_walls(maze: dict, x_coordinate: int, y_coordinate: int) -> tuple[bool, bool, bool, bool]:
    horizontal_array = find_horizontal_wall(maze, x_coordinate, y_coordinate)
    vertical_array = find_vertical_wall(maze, x_coordinate, y_coordinate)
    returnArray = [horizontal_array[0], vertical_array[0], horizontal_array[1], vertical_array[1]]

    return tuple(returnArray)


def find_horizontal_wall(maze: dict, x_coordinate: int, y_coordinate: int) -> list[bool]:
    horizontal_array = [False, False]
    if (x_coordinate, y_coordinate+1) in maze["walls"]["horizontal"]: #north wall
        horizontal_array[0] = True
    if (x_coordinate, y_coordinate) in maze["walls"]["horizontal"]: #south wall
        horizontal_array[1] = True  

    return horizontal_array

def find_vertical_wall(maze: dict, x_coordinate: int, y_coordinate: int) -> list[bool]:
    vertical_array = [False, False]
    if (y_coordinate, x_coordinate+1) in maze["walls"]["vertical"]: #east wall
        vertical_array[0] = True
    if (y_coordinate, x_coordinate) in maze["walls"]["vertical"]: #west wall
        vertical_array[1] = True  

    return vertical_array
        