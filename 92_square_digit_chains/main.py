# 44 (16+16) -> 32 (9+4) -> 13 (1+9) -> 10 (1+0) -> 1 -> 1

# start: 1
# end: 9_999_999

# Zalozmy ze mamy liczby 3 cyfrowe <100, 999>.
# f(n) -> suma kwadratow cyfr liczby n

# a, b, c in <1, 9>
# a * 100 + b * 10 + c

# f(a * 100 + b * 10 + c) = a^2 + b^2 + c^2 in <d, d * 81>

# 7 cyfr, d = 7
# f(n) in <7, 7 * 81> = <7, 567>

cap = 7 * 81
cache = [None for _ in range(cap+1)]

def f(n: int) -> int:
    s = 0
    while n:
        n, d = divmod(n, 10)
        s += d * d
    return s

def classify(n: int) -> int:
    chain = []
    while n != 1 and n != 89:
        if n <= cap and cache[n] is not None:
            n = cache[n]
            break
        if n <= cap:
            chain.append(n)
        n = f(n)
    for v in chain:
        cache[v] = n
    return n

print(sum(1 for i in range(1, 9_999_999+1) if classify(i) == 89))
