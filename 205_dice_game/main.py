# Peter 9 four-sided dice
# Colin 6 six-sided dice

from collections import defaultdict
import time


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

    start = [1 for _ in range(ndices)]
    # Create a dictionary of the dice's sums and the number of times they occur
    d: defaultdict[int, int] = defaultdict(int)
    s = ndices
    d[s] += 1
    while True:
        if all(x == maxdigit for x in start):
            break
        elif start[0] == maxdigit:
            # find first not maxdigit index
            idx = min([idx for idx, val in enumerate(start[1:]) if val != maxdigit])
            idx += 1
            start[idx] += 1
            s += 1
            for i in range(idx):
                s -= maxdigit - 1
                start[i] = 1
        else:
            start[0] += 1
            s += 1
        d[s] += 1
    return d


# def test():
#    d1 = [1 / 4 for _ in range(4)]
#    d1_cpy = d1[:]
#    for i in range(8):
#        d1 = np.convolve(d1, d1_cpy)
#    d2 = [1 / 6 for _ in range(6)]
#    d2_cpy = d2[:]
#    for i in range(5):
#        d2 = np.convolve(d2, d2_cpy)
#    print(d1)
#    print(d2)

if __name__ == "__main__":
    """This method does not rely on random numbers,
    only on math, so it gives the same and correct answer
    every time."""
    start = time.time()
    s1 = get_dice_sums(9, 4)
    s2 = get_dice_sums(6, 6)
    omega1 = 4 ** 9
    omega2 = 6 ** 6
    total = 0.0

    for sum1 in s1:
        # calculate how many dice rolls the current sum beats
        how_many_beats = sum([v for k, v in s2.items() if k < sum1])
        total += s1[sum1] / omega1 * how_many_beats / omega2
    print(f"The probability that Peter beats Colin is: {round(total, 7)}")
    print(f"Time taken: {round(time.time() - start, 3)}")
