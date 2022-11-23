#include <stdio.h>

/*
[[ a, b, c, d],
  [e, f, g, h],
  [i, j, k, l],
  [m, n, o, p]
 ]

diagonals
a + f + k + p = S
d + g + j + m = S
a + f + k + p = d + g + j + m
p = d + g + j + m - a - f - k

a + b + c + d = S
a + e + i + m = S
-----------------
b + c + d - e - i - m = 0
m = b + c + d - e - i

e + f + g + h = S
b + f + j + n = S
-----------------
e + g + h - b - j - n = 0
n = e + g + h - b - j

i + j + k + l = S
c + g + k + o = S
-----------------
i + j + l - c - g - o = 0
o = i + j + l - c - g


m + n + o + p = S
d + h + l + p = S
-----------------
m + n + o - d - h - l = 0
l = m + n + o - d - h


m = b + c + d - e - i
n = e + g + h - b - j
o = i + j + l - c - g
l = m + n + o - d - h
p = d + g + j + m - a - f - k

[[ a, b, c, d],
  [e, f, g, h],
  [i, j, k, l],
  [m, n, o, p]
 ]

S = a + b + c + d
h = S - g - f - e
l = S - k - j - i
p = S - o - n - m
o = S - k - g - c
n = S - j - f - b
m = S - i - e - a
j = a + e + i - d - g
k = o + n + m - f - a

[[ a, b, c, d],
  [e, f, g, S - g - f - e],
  [i, a + e + i - d - g, o + n + m - f - a, S - k - j - i],
  [S - i - e - a, S - j - f - b, S - k - g - c, S - o - n - m]
 ]
 */

int main(void) {
    int cnt = 0;
    for (int a = 0; a <= 9; a++) {
        for (int b = 0; b <= 9; b++) {
            for (int c = 0; c <= 9; c++) {
                for (int d = 0; d <= 9; d++) {
                    int S = a + b + c + d;
                    for (int e = 0; e <= 9; e++) {
                        for (int f = 0; f <= 9; f++) {
                            for (int g = 0; g <= 9; g++) {
                                int h = S - g - f - e;
                                if (h < 0 || h > 9) {
                                    continue;
                                }
                                for (int i = 0; i <= 9; i++) {
                                    int j = a + e + i - d - g;
                                    int m = S - i - e - a;
                                    int n = S - j - f - b;
                                    if (j < 0 || j > 9 || m < 0 || 
                                            m > 9 || n < 0 || n > 9) {
                                        continue;
                                    }
                                    for (int k = 0; k <= 9; k++) {
                                        int o = S - k - g - c;
                                        int l = S - k - j - i;
                                        int p = S - o - n - m;
                                        if (l < 0 || l > 9 || o < 0 || 
                                                o > 9 || p < 0 || p > 9) {
                                            continue;
                                        }
                                        cnt++;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    printf("%d\n", cnt);
    return 0;
}
