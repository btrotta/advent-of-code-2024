from utilities import *
from math import prod

arr = parse_single_string(False)

robots = []
for a in arr:
    p, v = a.split(" ")
    curr_robot = []
    for b in [p, v]:
        x, y = b.split(",")
        x = int(x[2:])
        y = int(y)
        curr_robot.append([x, y])
    robots.append(curr_robot)

x_lim, y_lim = 101, 103

quadrant_counts = [0, 0, 0, 0]
for r in robots:
    px, py = r[0]
    vx, vy = r[1]
    px = (px + 100 * vx) % x_lim
    py = (py + 100 * vy) % y_lim
    if px == x_lim // 2 or py == y_lim // 2:
        continue
    quad = 0
    if px > x_lim // 2:
        quad = 2
    if py > y_lim // 2:
        quad += 1
    quadrant_counts[quad] += 1

ans = prod(quadrant_counts)
print(ans)
