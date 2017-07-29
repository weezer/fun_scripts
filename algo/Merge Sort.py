def merge_sort(lst):
    lst_len = len(lst)
    if lst_len <= 1:
        return lst
    left_part = merge_sort(lst[:lst_len/2])
    right_part = merge_sort(lst[lst_len/2:])
    pos = 0
    l_pos = 0
    r_pos = 0
    left_len = len(left_part)
    right_len = len(right_part)
    while l_pos < left_len and r_pos < right_len:
        if left_part[l_pos] < right_part[r_pos]:
            lst[pos] = left_part[l_pos]
            l_pos += 1
        else:
            lst[pos] = right_part[r_pos]
            r_pos += 1
        pos += 1

    if l_pos < left_len:
        lst[pos:] = left_part[l_pos:]
    if r_pos < right_len:
        lst[pos:] = right_part[r_pos:]
    return lst

print merge_sort([])
