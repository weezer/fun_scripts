def greedy(input):
    rating = 26
    pair = {}
    perfection = 0
    for i in input:
        if pair.get(i.lower()):
            pair[i.lower()] = pair[i.lower()] + 1
        else:
            pair[i.lower()] = 1
    pair = sorted(pair.iteritems(), key = lambda d: d[1], reverse=True)
    for k, v in pair:
        perfection += v * rating
        rating -= 1
    return perfection


print greedy("EYBQTBTKQJ")