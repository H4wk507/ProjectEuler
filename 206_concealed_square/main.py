# we have a square number: n^2 = 1x2x3x4x5x6x7x8x9x0

# 1020304050607080900 <= n^2 <=
# 1929394959697989900
# 1010101011 <= n <=
# 1389026623

# n^2 is divisible by 4 and 25 => (100 | n^2) => (10 | n)
# n ends with 0 so we can start with number divisible by 10
# and check every 10th number
# there are 378_925_621 numbers from 1010101010 to 1389026630
# but we check every 10th number so the are 37_892_562 numbers to check


def get_ndigit(number: str, n: int) -> str:
    return number[-1 - n]


def test(number: str) -> bool:
    return (
        get_ndigit(number, 2) == "9"
        and get_ndigit(number, 4) == "8"
        and get_ndigit(number, 6) == "7"
        and get_ndigit(number, 8) == "6"
        and get_ndigit(number, 10) == "5"
        and get_ndigit(number, 12) == "4"
        and get_ndigit(number, 14) == "3"
        and get_ndigit(number, 16) == "2"
        and get_ndigit(number, 18) == "1"
    )


MIN = 1010101010
MAX = 1389026630
if __name__ == "__main__":
    for i in range(MIN, MAX + 1, 10):
        str_i = str(i * i)
        if test(str_i):
            print(i, str_i)
            break
