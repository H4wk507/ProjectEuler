"""
Let a, b ∈ N and a, b < 100.
Consider all numbers in the form a^b.
What is the maximum digital sum possible?

99 * 99 = 9801 numbers to consider

The sum of digits is chaotic. There is no closed form solution of the type S(a^b).
So we just brute force it.
"""

print(
    max(
        sum(int(digit) for digit in str(a**b))
        for b in range(1, 100)
        for a in range(1, 100)
    )
)
