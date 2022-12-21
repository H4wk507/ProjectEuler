// 1 digit no solution, obvious, n + n is even

// 2 digits 10n+m, 10n+m + 10m+n = 11(n+m)
// n + m must be odd, so n or m must be odd but not both
// if n odd and m even, we have 20 numbers

// 3 digits 100n+10m+p, 100n+10m+p + 100p+10m+n = 101n+20m+101p = 101(n+p)+20m
// if m == 0, (2,9 3,8, 4,7, 5,6, 4,9, 5,8, 6,7, 6,9, 7,8, 8,9), 50*2 = 100
// if m >= 5, 0

// 4 digits 1000n+100m+10p+q, 1000n+100m+10p+q + 1000q+100p+10m+n = 1001n+1001q+110m+110p
// = 1001(n+q)+110(m+p), n+q must be odd and m+p must be odd so 20*25=500 numbers
// dla sum n+q, m+p < 10, (1,2, 1,4, 1,6, 1,8, 3,2, 3,4, 3,6, 5,2, 5,4, 7,2), 10*2*15*2=600
// dla sum n+q, m+p > 10, 0,

// 5 digits 10000n+1000m+100p+10q+s + 10000s+1000q+100p+10m+n
// = 10001n+10001s+1010m+1010q+200p = 10001(n+s)+1010(m+q)+200p
// m+q > 10 to get rid of middle 0, but then leading digit is even
// so n+s must be even, but then trailing zero is even, which is wrong, no solution.

// 6 digits 100_000n+10_000m+1000p+100q+10s+t + 100_000t+10_000s+1000q+100p+10m+n
// = 100_001n+100_001t+10_010m+10_010s+1100p+1100q = 100_001(n+t)+10_010(m+s)+1_100(p+q)
// n+t, m+s, p+q must be odd, it's just 4digits case * 30 10*2*15*2*15*2 = 18_000

// 7 digits 1_000_000n+100_000m+10_000p+1000q+100s+10t+o + 1_000_000o+100_000t+10_000s+1000q+100p+10m+n
// 1_000_001(n+o)+
//   100_010(m+t)+
//    10_100(p+s)+
//     2_000q
// q < 5, 10*2*10*2*5*25 = 50_000

// 8 digits, same as 6 digits but *15*2 = 540_000

// 9 digits, same as 5 digits, no solution

fn main() {
    let cnt: u32 = 0 + 20 + 100 + 600 + 0 + 18_000 + 50_000 + 540_000 + 0;
    println!("{}", cnt);
}
