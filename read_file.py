filename = raw_input()
with open(filename) as file:
    lines = file.readlines()
    print lines[0]

