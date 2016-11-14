a = [1,1,5]

# adict = {}
# for i in a:
#     if adict.has_key(i):
#         adict[i] += 1
#     else:
#         adict[i] = 1
#
# for k, i in adict.items():
#     if i == 1:
#         print k
#

b = 0
for i in a:
    b ^= i

print b