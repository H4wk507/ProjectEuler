# Peter 9 four-sided dice
# Colin 6 six-sided dice

from collections import defaultdict
import numpy as np


def run_sample(wsamples: int) -> int:
    ptotal = np.sum(np.random.randint(1, 5, size=9))
    ctotal = np.sum(np.random.randint(1, 7, size=6))
    wsamples += ptotal > ctotal
    return wsamples


def old_method() -> None:
    """Gives the correct answer to like 3 decimal places,
    otherwise it's too slow."""
    wsamples = 0
    t = 100_000
    for _ in range(t):
        wsamples = run_sample(wsamples)
    print(round(wsamples / t, 7))


def get_dice_sums(ndices: int, maxdigit: int) -> defaultdict[int, int]:
    """Returns a dictionary of the sums of the dice and the number of
    times they occur."""

    # Generate all combinations of rolling ndices
    start = [1 for _ in range(ndices)]
    combinations = [start[:]]
    while True:
        if all(x == maxdigit for x in start):
            break
        elif start[0] == maxdigit:
            # find first not maxdigit index
            idx = min(
                [idx for idx, val in enumerate(start[1:]) if val != maxdigit]
            )
            idx += 1
            start[idx] += 1
            for i in range(idx):
                start[i] = 1
        else:
            start[0] += 1
        combinations.append(start[:])
    # Create a dictionary of the dice's sums and the number of times they occur
    d: defaultdict[int, int] = defaultdict(int)
    for comb in combinations:
        d[sum(comb)] += 1
    return d


if __name__ == "__main__":
    """This method does not rely on random numbers,
    only on math, so it gives the same and correct answer
    every time."""
    s1 = get_dice_sums(9, 4)
    s2 = get_dice_sums(6, 6)
    omega1 = 4 ** 9
    omega2 = 6 ** 6
    total = 0.0

    for sum1 in dict(s1):
        # calculate how many dice rolls the current sum beats
        how_many_beats = sum([v for k, v in dict(s2).items() if k < sum1])
        total += s1[sum1] / omega1 * how_many_beats / omega2
    print(f"The probability that Peter beats Colin is: {round(total, 7)}")
