#wRITE ALL POSSIBLE SUBSETS OF A SET , don't print dups
# [1,2] should pring [1] [2] [1 2] []

def findPowerSet(S):
    # Total number of element in the power set will be power(2,lenghtof the Set) in this case it is pow(2,3) =8
    N = int(pow(2, len(S)))
    s1 = set()

    # sort the set --in this case 1,3,4
    S.sort()

    # generate each subset one by one loop 8 times outside for each element and then  for each value scan the array from left to right
    for i in range(N):
        subset = []
        # check every bit of `i`
        for j in range(len(S)):
            # if j'th bit of `i` is set, append `S[j]` to the subset
            if i & (1 << j):
                subset.append(S[j])

        # insert the subset into the set
        s1.add(str(subset))

    # print all subsets present in the set
    for subset in s1:
        print(subset)


if __name__ == '__main__':
    S = [4, 2, 3]

    findPowerSet(S)