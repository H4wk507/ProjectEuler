"""
A number n is circular prime if it's prime and all its rotations are prime.
For example: 197, 719, 971 are circular primes.

How many are there < 1_000_000?
n ∈ { 1, 2, ..., 999_999 }

If number n has d digits, then it has d rotations.

Prime number n can't end with { 2, 4, 5, 6, 8 } because that implies that its
even or is divisible by 5.
So for n to be prime, the last digit must be in { 1, 3, 7, 9 }.

But if we consider all rotations to be prime, then all digits in the number
must be in { 1, 3, 7, 9 }.

We need to consider all numbers, that have all of its digits from this
set, and check whether they are circular.
"""

from itertools import product

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def is_circular(n: int) -> bool:
    s = str(n)
    return all(is_prime(int(s[i:] + s[:i])) for i in range(len(s)))


cnt = 4 # 2, 3, 5, 7
for d in range(2, 7):
    for digits in product("1379", repeat=d):
        n = int("".join(digits))
        if is_circular(n):
            cnt += 1

print(cnt)
