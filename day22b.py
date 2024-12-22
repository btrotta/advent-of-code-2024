from utilities import *

arr = parse_single_int(False)

prune = lambda x: x % 16777216


def step(x):
    x = prune(x ^ (x * 64))
    x = prune(x ^ (x // 32))
    x = prune(x ^ (x * 2048))
    return x


sequences = []
diffs = []
for a in arr:
    sequences.append([])
    diffs.append([])
    for i in range(2000):
        a = step(a)
        sequences[-1].append(a % 10)
        if i > 0:
            diffs[-1].append(sequences[-1][-1] - sequences[-1][-2])

buyer_bananas_with_sequence = []
for buyer_idx, (prices, diff) in enumerate(zip(sequences, diffs)):
    buyer_bananas_with_sequence.append({})
    for i in range(len(diff) - 3):
        seq = diff[i: i+4]
        profit = prices[i+4]
        if tuple(seq) not in buyer_bananas_with_sequence[buyer_idx]:
            buyer_bananas_with_sequence[buyer_idx][tuple(seq)] = profit

total_profit_with_sequence = defaultdict(lambda: 0)
for buyer_idx in range(len(buyer_bananas_with_sequence)):
    for seq, profit in buyer_bananas_with_sequence[buyer_idx].items():
        total_profit_with_sequence[seq] += profit
ans = max(total_profit_with_sequence.values())
print(ans)
