# a, b ∈ {2, 3, 4, 5}
# Consider all combinations of a^b. 4*4 = 16 such combinations.
# However if we remove duplicates, we get 15 such combinations, because
# 4^2 = 2^4 = 16.

# Given a, b ∈ {2, 3, ..., 100}
# Count how many unique values of a^b are there.

# 99*99 = 9801 combinations to generate.

# Observation: every natural number (>1) can be uniquely represented as a product
# of prime numbers (fundamental theorem of arithmetic). a = p_1^e_1 * p_2^e_2 * ... p_n^e_n.
# a^b = (p_1^e_1 * p_2^e_2 * ... p_n^e_n)^b = p_1^(e_1*b) * p_2^*(e_2*b) * ... p_n^(e_n*b)

# So, a number a^b is uniquely described by a set of pairs (p, e*b).
# If some other number c^d is also described by the same set of pairs (p, e*b).
# That means that a^b = c^d, based on fundamental theorem of arithmetic.

# That way we don't need to compute big powers. We just build a set
# (removes duplicates) of these fingerprints, and its size is the answer.


def prime_factorization(n: int) -> dict[int, int]:
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def fingerprint(factors: dict[int, int], b: int) -> tuple[int, int]:
    return tuple(sorted((p, e * b) for p, e in factors.items()))


start = 2
end = 100
factors = {a: prime_factorization(a) for a in range(start, end + 1)}
print(
    len(
        {
            fingerprint(factors[a], b)
            for a in range(start, end + 1)
            for b in range(start, end + 1)
        }
    )
)
