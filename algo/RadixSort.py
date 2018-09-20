#!/usr/bin/python'

import math


def radix_sort(nums, radix=10):
    k = int(math.ceil(math.log(max(nums)+1, radix)))
    for i in range(1, k+1):
        bucket = [[] for _ in range(radix)]
        for val in nums:
            bucket[(val % (radix ** i)) // (radix ** (i - 1))].append(val)
        print bucket
        del nums[:]
        for k in bucket:
            nums.extend(k)
    return nums

print radix_sort([13,6,9,100])