
for i in range(8):

    # check every bit of `i`
    for j in range(3):
        # if j'th bit of `i` is set, append `S[j]` to the subset
        if i & (1 << j):
            print(bin(i),bin(j),(i & (1 << j)))