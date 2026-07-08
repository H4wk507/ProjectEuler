# 1p, 2p, 5p, 10p, 20p, 50p, 100p, 200p

# we can make 200p by linear combination: 1*100p + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p

# how many different linear combinations for 200p?

# p ∈ N

# a + 2b + 5c + 10d + 20e + 50f + 100g + 200h = 200
# How many solutions?

# a = 200 - 2b - 5c - 10d - 20e - 50f - 100g - 200h ∈ Z
# We take only a ∈ N, so >= 0

# a ∈ {0, 1, 2, ..., 200}
# b ∈ {0, 1, 2, ..., 100}
# c ∈ {0, 1, 2, ..., 40}
# d ∈ {0, 1, 2, ..., 20}
# e ∈ {0, 1, 2, ..., 10}
# f ∈ {0, 1, 2, ..., 4}
# g ∈ {0, 1, 2}
# h ∈ {0, 1}

# TODO: use dynamic programming

cnt = 0 
for b in range(101):
    for c in range(41):
        for d in range(21):
            for e in range(11):
                for f in range(5):
                    for g in range(3):
                        for h in range(2):
                            a = 200 - 2*b - 5*c - 10*d - 20*e - 50*f - 100*g - 200*h
                            if a >= 0:
                                cnt += 1
print(cnt)
