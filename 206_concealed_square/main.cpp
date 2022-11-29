#include <iostream>
#include <cmath>

using namespace std;

int get_ndigit(long long number, int n) {
    /* get nth-digit from the right, 0 indexed */
    return static_cast<long long>(number / powl(10L, n)) % 10L;
}

bool test(long long number) {
    return 
        get_ndigit(number, 2) == 9  &&
        get_ndigit(number, 4) == 8  &&
        get_ndigit(number, 6) == 7  &&
        get_ndigit(number, 8) == 6  &&
        get_ndigit(number, 10) == 5 &&
        get_ndigit(number, 12) == 4 &&
        get_ndigit(number, 14) == 3 &&
        get_ndigit(number, 16) == 2 &&
        get_ndigit(number, 18) == 1;

}

const long long MIN = 1010101010;
const long long MAX = 1389026630;

int main(void) {
    long long i, ipow;

    for (i = MIN; i <= MAX; i += 10) {
        ipow = i * i;
        if (test(ipow)) {
            cout << i << ' ' << ipow << '\n';
            break;
        }
    }
    return 0;
}
