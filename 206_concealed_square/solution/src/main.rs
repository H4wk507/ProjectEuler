const MIN: u64 = 1010101010;
const MAX: u64 = 1389026630;

fn get_ndigit(num: u64, n: u32) -> u64 {
    return (num / u64::pow(10, n)) % 10;
}

fn test(num: u64) -> bool {
    return get_ndigit(num, 2) == 9 &&
        get_ndigit(num, 4) == 8 &&
        get_ndigit(num, 6) == 7 &&
        get_ndigit(num, 8) == 6 &&
        get_ndigit(num, 10) == 5 &&
        get_ndigit(num, 12) == 4 &&
        get_ndigit(num, 14) == 3 &&
        get_ndigit(num, 16) == 2 &&
        get_ndigit(num, 18) == 1;
}

fn main() {
    let mut ipow: u64;
    for i in (MIN..MAX).step_by(10) {
        ipow = i * i;
        if test(ipow) {
            println!("{} {}", i, ipow);
            break;
        }
    }
}
