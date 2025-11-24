def create_runner(x: int, y: int, orientation: str) -> dict:
    return {"x": x, "y": y, "orientation": orientation}

def get_x(runner: dict) -> int:
    return runner["x"]

def get_y(runner: dict) -> int:
    return runner["y"]

def get_orientation(runner: dict) -> str:
    return runner["orientation"]

def turn(runner: dict, direction: str) -> dict:
    orientations = ['N', 'E', 'S', 'W']
    i = orientations.index(runner["orientation"])

    if direction == "Right":
        i = (i + 1) % 4
    else:
        i = (i - 1) % 4

    runner["orientation"] = orientations[i]
    return runner



def forward(runner: dict) -> dict:
    if runner["orientation"] == 'N':
        runner["y"] += 1
    elif runner["orientation"] == 'E':
        runner["x"] += 1
    elif runner["orientation"] == 'S':
        runner["y"] -= 1
    elif runner["orientation"] == 'W':
        runner["x"] -= 1
    return runner


