/*
A number n is a curious number if the sum of the factorials of its digits is
equal to n. For example 145 = 1! + 4! + 5! = 145. Find the sum of all curious
numbers.

If number n has d digits, then n ∈ <10^(d-1), 10^d-1>. The factorial sum of n is from <d, d * 9!> = <d, d * 362880>.

10^(d-1) grows faster than d * 362880. So after a certain d, the smallest d-digit
number will be greater than the largest factorial sum of d digits.

d ∈ N
10^(d-1) > d * 362880 <=> d - 1 > log10(d * 362880) => d_min = 8

Smallest d ∈ N that satisfy the inqueality is 8. So the smallest 8 digit number
10_000_000 is higher than the largest factorial sum for 8 digit number
8 * 362880 = 2_903_040. So we need to check numbers up to 7 * 362880.
*/

#include <iostream>
#include <cstdint>

using u32 = std::uint32_t;

inline constexpr int F[] = { 1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880 };

int main() {
    u32 total = 0;
    for (u32 n = 10; n <= 2'540'160; n++) {
        u32 s = 0, m = n;
        while (m) {
            s += F[m % 10];
            m /= 10;
        }
        total += (s == n) * n;
    }
    std::cout << total << '\n';
}
