from utilities import *

arr = parse_single_string(False)
machines = []
curr_machine = []
for a in arr:
    if a.startswith("Button A") or a.startswith(("Button B")):
        x, y = a.split(" ")[-2:]
        x = int(x[1:-1])
        y = int(y[1:])
        curr_machine.append(np.array([x, y]))
    elif a.startswith("Prize"):
        x, y = a.split(" ")[-2:]
        x = int(x[2:-1]) + 10000000000000
        y = int(y[2:]) + 10000000000000
        curr_machine.append(np.array([x, y]))
        machines.append(curr_machine)
        curr_machine = []


def find_integer_factor(a, b):
    c = b / a
    if np.all(np.round(c[0], 0) * a == b) and c[0] >= 0:
        return np.round(c[0], 0).astype(np.int64)
    else:
        return None


ans = 0
for m in machines:
    X = np.array([m[0], m[1]]).transpose()
    y = np.array(m[2])
    try:
        res = np.linalg.solve(X, y)
        res = np.round(res, 0).astype(np.int64)
        if np.all(m[2] == res[0] * m[0] + res[1] * m[1]) and np.min(res) >= 0:
            ans += 3 * res[0] + res[1]
    except:
        # one button's values must be a multiple of the other's
        # this case doesn't seem to occur in the input
        f0 = find_integer_factor(m[0], m[2])
        f1 = find_integer_factor(m[1], m[2])
        if f0 is None:
            if f1 is not None:
                ans += f1
        elif f1 is None:
            if f0 is not None:
                ans += f0 * 3
        else:
            ans += min(f0 * 3, f1)

print(ans)

