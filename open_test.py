def build_bucket(filename):
    d = {}
    with open(filename, 'r') as f:
        for line in f:
            word = line[:-1]
            for i in range(len(word)):
                key_word = word[:i] + "_" + word[i+1:]
                if d.get(key_word):
                    d[key_word].append(word)
                else:
                    d[key_word] = [word]


build_bucket("4letter.txt")