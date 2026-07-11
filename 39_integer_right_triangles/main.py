"""
Let p be a perimeter of a right angle triangle with sides { a, b, c } ∈ N.
There are 3 solutions for p = 120. { 20, 48, 52 }, { 24, 45, 51 }, { 30, 40, 50 }.
Which p <= 1000 has the most number of solutions?

p = a + b + c
a^2 + b^2 = c^2

Using Euclid's formula (scaled)
a = k(m^2 - n^2)
b = 2kmn
c = k(m^2 + n^2)
m, n ∈ N, m > n

To generate each triple exactly once, m, n must generate primitives:
gcd(m, n) = 1 (coprime)
m - n is odd  (opposite parity)
Without these two conditions the same triple is generated multiple times
{ 12, 16, 20 }: (m=4,n=2,k=1) and (m=2,n=1,k=4) -> overcounts.

p = km^2 - kn^2 + 2kmn + km^2 + kn^2 = 2km^2 + 2kmn = 2km(m+n)

Upper bound on m: We set n = 1 and k = 1 => p <= 1000 <=> 2m(m+1) <= 1000 => m <= 21.
"""

from math import gcd
from collections import defaultdict

cap = 1000
p_to_n = defaultdict(int)

for m in range(1, 22):
    for n in range(1, m):
        if (m - n) % 2 == 1 and gcd(m, n) == 1:
            p = 2*m*(m+n)
            k = 1
            while k * p <= cap:
                p_to_n[k * p] += 1
                k += 1

print(sorted(p_to_n.items(), key=lambda kv: kv[1], reverse=True)[0])
