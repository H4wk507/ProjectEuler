"""
A d-digit number is pandigitial if it makes use of all the digits from 1 to
d exactly once. For example 2143 is a 4-digit pandigital and is also prime.

What is the largest pandigital prime?

Upper bound on pandigital numbers is a 9-digit number 987654321.

Number of pandigital numbers:
For d-digit number we have a set { 1, 2, ..., d } of possible digits. We
generate all permutations of this set, to get all pandigital numbers. d!
possible numbers.

1! + 2! + ... + 9! = 409,113 pandigitals to consider.

But knowing that they also must be prime, can we reduce the search space?
Let's consider 2-digit pandigital number n. Its sum of digits is always
1 + 2 = 3. But if sum of digits is divisible by 3, that means it's divisible by
3, so it can't be prime.

For d = 3, we have 1 + 2 + 3 = 6.
For d = 5, we have 1 + 2 + 3 + 4 + 5 = 15.
For d = 6, we have 1 + 2 + 3 + 4 + 5 + 6 = 21.
For d = 8, we have 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36.
For d = 9, we have 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45.

So those d-digit pandigitals can't be prime, because their sum of digits
is divisible by 3, making it divisible by 3.

So we only need to consider d ∈ { 1, 4, 7 }. 1! + 4! + 7! = 5065.

As we know the upper bound, we can start iterating from the top to bottom
and the first prime pandigital is our answer, as it is the largest.
"""

from itertools import permutations

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

for d in (7, 4, 1):
    digits = ''.join(str(i) for i in range(d, 0, -1))
    for perm in permutations(digits):
        n = int(''.join(perm))
        if is_prime(n):
            print(n)
            break
    else:
        continue
    break
