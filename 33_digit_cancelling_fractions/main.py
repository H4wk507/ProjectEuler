"""
49/98 is 'curious' fraction, because you can incorrectly cancel out
'9's and get 4/8, which is correct.

Skip trivial examples like 30/50

there are 4 non-trivial examples, which are less than 1 and
that have 2 digits in numerator in denominator.

find value of denominator of product of those 4 examples.

---

numerator and denominator must have 2 digits so:
numerator   ∈ {10, 11, ..., 99}
denominator ∈ {10, 11, ..., 99}

90 * 90 = 8100 combinations to check
but numerator < denominator, so 0 + 1 + 2 + ... + 89 = 4005 combinations to check

(a * 10 + b) / (c * 10 + d)

--- let's cancel 'a' from numerator

b / (c * 10 + d)

then from denominaor we have 2 cases

b / (c * 10)
b / d

--- let's cancel 'b' from numerator

(a * 10) / (c * 10 + d)

then from denominaor we have 2 cases

(a * 10) / (c * 10)
(a * 10) / d

this fraction is curious, if either one of those 4 canceled
fractions

b / (c * 10)
b / d
(a * 10) / (c * 10)
(a * 10) / d

is actually equal to numeric value of the fraction.
"""

from fractions import Fraction


def equal(n1: int, d1: int, n2: int, d2: int) -> bool:
    """n1/d1 == n2/d2 <=> n1 * d2 == n2 * d1"""
    return n1 * d2 == n2 * d1


prod = Fraction(1)

for num in range(10, 100):
    for den in range(num + 1, 100):
        # num = a * 10 + b
        # den = c * 10 + d
        a, b, c, d = num // 10, num % 10, den // 10, den % 10
        # trivial cases
        if b == 0 and d == 0:
            continue
        # remove first digit from num and second from den
        if a == d and equal(num, den, b, c):
            prod *= Fraction(num, den)
        # remove first digit from num and first from den
        elif a == c and equal(num, den, b, d):
            prod *= Fraction(num, den)
        # remove second digit from num and second from den
        elif b == d and equal(num, den, a, c):
            prod *= Fraction(num, den)
        # remove second digit from num and first from den
        elif b == c and equal(num, den, a, d):
            prod *= Fraction(num, den)


print(prod.denominator)
