/*
The series 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
Find last 10 digits of 1^1 + 2^2 + 3^3 + ... + 1000^1000.
In other words, calculate (1^1 + 2^2 + 3^3 + ... + 1000^1000) % (10^10)

Some modular arithmetic laws:
(a_1 + a_2 + ... + a_k) % m = ((a_1 % m) + (a_2 % m) + ... + (a_k % m)) % m
(a^b) % m = ((a % m)^b) % m

By using the addition law, we get
(1^1 + 2^2 + ... + 1000^1000) % 10^10 =
((1^1)%m + (2^2)%m + ... + (1000^1000)%m) % m

That won't help us, because we still have to calculate big powers like
1000^1000 in the first place.

We could try to use the exponentiation law, but it only lets us shrink the base
(a % m). Here the base is already small, it's the exponent that's huge.

The trick is to trade a big exponent for repeated squaring, using two simple
identities
- a^(2k) = (a^k)^2
- a^(2k+1) = a * (a^k)^2

So if exponent is even, we halve it and square the running power. If it's odd,
we peel off one factor of a and then halve the rest. Each step at least halves
the exponent, so we drop b multiplications down to about log2(b).
*/

#include <iostream>
#include <cstdint>

using u64 = std::uint64_t;

u64 modpow(u64 a, u64 b, u64 m) {
    u64 res = 1;
    a %= m;
    while (b > 0) {
        if (b & 1) {
            res = (unsigned __int128)res * a % m;
        }
        a = (unsigned __int128)a * a % m;
        b >>= 1;
    }
    return res;
}


int main() {
    u64 s = 0;
    u64 cap = 1000;
    u64 m = 10000000000;
    for (u64 n = 1; n <= cap; n++) {
        s = (s + modpow(n, n, m)) % m;
    }
    std::cout << s << '\n';
}
