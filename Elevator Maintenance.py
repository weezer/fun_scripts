def version_sort(list):
    version_list = []
    for i in list:
        version_list.append(i.split("."))
    for i in range(len(version_list)):
        for j in range(i):
            if i == 3:
                print version_list
            if elem_compare(version_list[i], version_list[j]):
                version_list[i], version_list[j] = version_list[j], version_list[i]
    result = []
    for i in version_list:
        result.append(".".join(i))
    return result


def elem_compare(a, b):
    for i in range(min(len(a), len(b))):
        if a[i] < b[i]:
            return True
        if a[i] > b[i]:
            return False
    return (True, False)[len(a) > len(b)]


print version_sort(["5", "5.2", "1", "1.0", "1.0.0", "2"])

