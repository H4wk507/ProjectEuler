"""
Conjecture: Every odd composite number can be written as the sum of a prime
and twice a square.
For example:
9 = 7 + 2 * 1^2
15 = 7 + 2 * 2^2
21 = 3 + 2 * 3^2
25 = 7 + 2 * 3^2
27 = 19 + 2 * 2^2
33 = 31 + 2 * 1^2
n = p + 2 * a^2

It turns out, that this conjecture is false.
What is the smallest counterexample?

Counterexample is an odd composite number, that can't be written as the sum of
a prime and twice a square.

We iterate over odd, composite numbers. For number n, we check a from 1 to
n - 2 * a^2. We calculate p = n - 2 * a^2. If for every a in that range p is
not prime, then n can't be written as the sum of a prime and twice a square.
So this is our counterexample.
"""

from math import isqrt
from itertools import count


def is_counterexample(n: int) -> bool:
    return not any(is_prime(n - 2 * a * a) for a in range(1, isqrt(n // 2) + 1))


def is_prime(n: int) -> bool:
    return all(n % i != 0 for i in range(2, isqrt(n) + 1))


print(next(n for n in count(9, 2) if not is_prime(n) and is_counterexample(n)))
