def OneEditDistance(lst1, lst2):
    len_lst = len(lst1)
    if len_lst - len(lst2) > 1:
        return False
    diff = 0
    for pos in len_lst:
        if lst1[pos] != lst2[pos + diff]:
            if diff == 0:
                if len_lst > len(lst2):
                    diff -= 1
                else:
                    diff += 1
            else:
                return False
    return True