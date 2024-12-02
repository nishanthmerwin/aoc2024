

from pathlib import Path
from collections import Counter

DATA_PATH = Path(__file__).parent.parent.parent / "data/d1.txt"


def solve_a(data_input):
    l1, l2 = [], []
    for line in data_input.split("\n"):
        vals = list(map(int, line.split()))
        l1.append(vals[0])
        l2.append(vals[1])

    l1, l2 = sorted(l1), sorted(l2)
    total_diff = 0
    for val1, val2 in zip(l1, l2):
        diff = abs(val1 - val2)
        total_diff += diff

    return total_diff

def solve_b(data_input):
    l1, l2 = [], []
    for line in data_input.split("\n"):
        vals = list(map(int, line.split()))
        l1.append(vals[0])
        l2.append(vals[1])

    l2_counts = Counter(l2)

    score = 0
    for val_a in l1:
        score += val_a * l2_counts.get(val_a, 0)

    return score


if __name__ == "__main__":

    with open(DATA_PATH) as fp:
        data_input = fp.read().strip()

    answer_a = solve_a(data_input)

    answer_b = solve_b(data_input)

    print(answer_b)

