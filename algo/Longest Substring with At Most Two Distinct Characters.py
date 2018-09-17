def twoDistinctCharacters(lst):
    len_lst = len(lst)
    ans_len = 0
    start_pos = -1
    pos_kv = {}
    ans_word = []
    for pos in range(len_lst):
        pos_kv[lst[pos]] = pos
        if len(ans_word) < 2 and lst[pos] not in ans_word:
            ans_word.append(lst[pos])
        if len(ans_word) == 2 and lst[pos] not in ans_word:
            start_pos = (pos_kv[ans_word[0]], pos_kv[ans_word[1]])[pos_kv[ans_word[0]] < pos_kv[ans_word[1]]] - 1
            ans_word.remove((ans_word[0], ans_word[1])[pos_kv[ans_word[0]] > pos_kv[ans_word[1]]])
            ans_word.append(lst[pos])
        ans_len = max(ans_len, pos - start_pos)
    return ans_len

a = "abcdef"
print twoDistinctCharacters(a)