def longest_consecutive_seq(lst):
    if len(lst) <= 1:
        return len(lst)
    seq_map = {}
    max_lcs = 0
    for i in lst:
        if seq_map.get(i) is None:
            seq_map[i] = i
            if seq_map.get(i+1) is not None:
                seq_map[i] = seq_map[i+1]
                seq_map[seq_map[i]] = i
                max_lcs = max(seq_map[i] - i, max_lcs)
            if seq_map.get(i-1) is not None:
                larger = seq_map[i]
                seq_map[seq_map[i]] = seq_map.get(i-1)
                smaller = seq_map.get(i-1)
                seq_map[seq_map[i-1]] = larger
                max_lcs = max(larger - smaller, max_lcs)
            print seq_map
    return max_lcs


print longest_consecutive_seq([100,4,200,1,3,2])
print longest_consecutive_seq([1,2,0,1])
print longest_consecutive_seq([-7,-1,3,-9,-4,7,-3,2,4,9,4,-9,8,-7,5,-1,-7])