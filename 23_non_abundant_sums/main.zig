const std = @import("std");

fn is_abundant(n: u32) bool {
    var sum: u32 = 0;
    const limit: i32 = @intFromFloat(@sqrt(@as(f32, @floatFromInt(n))));

    var i: u32 = 2;
    while (i <= limit) : (i += 1) {
        if (n % i == 0) {
            sum += i;
            if (i != n / i) {
                sum += n / i;
            }
        }
    }

    return sum > n;
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const allocator = arena.allocator();

    var abundants = std.ArrayList(u32).init(allocator);
    defer abundants.deinit();

    const LIMIT: u32 = 28123;

    for (12..LIMIT) |n| {
        if (is_abundant(@intCast(n))) {
            try abundants.append(@intCast(n));
        }
    }

    var can_be_summed = try std.bit_set.DynamicBitSet.initFull(allocator, LIMIT);
    defer can_be_summed.deinit();

    for (0..abundants.items.len) |i| {
        for (i..abundants.items.len) |j| {
            const sum = abundants.items[i] + abundants.items[j];
            if (sum < LIMIT) {
                can_be_summed.unset(sum);
            }
        }
    }

    var sum: u64 = 0;
    for (1..LIMIT) |n| {
        if (can_be_summed.isSet(n)) {
            sum += n;
        }
    }

    std.debug.print("{}\n", .{sum});
}
