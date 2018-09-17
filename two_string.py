
def commonSubstring(a, b):
    len_a = len(a)
    result = []
    for i in range(len_a):
        result.append(compare(a[i], b[i]))
    return result


def compare(a, b):
    letter = [0] * 26
    for pos in a:
        letter[ord(pos) - ord("a")] = 1
    for pos in b:
        if letter[ord(pos) - ord("a")]:
            return "YES"
    return "NO"

print commonSubstring(["hello", "hi"], ["world", "bye"])