from utilities import *
import matplotlib.pyplot as plt
import os

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

if not(os.path.exists("plots")):
    os.mkdir("plots")
s = 0
arr = np.zeros((x_lim, y_lim), dtype=np.int32)
for s in range(10000):
    x_count = [0, 0]
    y_count = [0, 0]
    for r in robots:
        px, py = r[0]
        vx, vy = r[1]
        arr[px, py] = 0
        px = (px + vx) % x_lim
        py = (py + vy) % y_lim
        r[0] = [px, py]
        arr[px, py] = 1
        x_half = px // (x_lim // 2 + 1)
        x_count[x_half] += 1
        y_half = py // (y_lim // 2 + 1)
        y_count[y_half] += 1

    # check for asymmetry
    if abs(x_count[0] - x_count[1]) > 100 or abs(y_count[0] - y_count[1]) > 100:
        plt.figure()
        plt.imshow(arr)
        plt.savefig(f"plots/fig_{s + 1}")
        plt.close()
