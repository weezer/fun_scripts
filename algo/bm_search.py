def bm_algo(s, p):
    letter_index = [{}] * len(p)
    for i in range(1, len(p)):
        letter_index[i] = letter_index[i-1].copy()
        letter_index[i][p[i-1]] = i-1
    suffix_index = [{}] * len(p)
    
