import heapq


def solution(input_list, k):
    count = 0
    h = []
    for i in input_list:
        if count < k:
            heapq.heappush(h, i)
            count += 1
        else:
            if i > h[0]:
                heapq.heapreplace(h, i)
    print h
    return h[0]


def solution2(input_list, k):
    return find_k(input_list, 0, len(input_list)-1, k-1)


def find_k(input_list, start, end, k):
    pivot = end
    first = start
    last = end - 1
    while first < last:
        while input_list[first] <= input_list[pivot] and first < last:
            first += 1
        while input_list[last] >= input_list[pivot] and last > first:
            last -= 1
        if first < last:
            tmp = input_list[first]
            input_list[first] = input_list[last]
            input_list[last] = tmp
            first += 1
    if input_list[first] > input_list[pivot]:
        tmp = input_list[first]
        input_list[first] = input_list[pivot]
        input_list[pivot] = tmp
    # print input_list, start, end, k
    if k == end - start:
        return input_list[end]

    if k >= first:
        return find_k(input_list, first, end-1, k - first)
    else:
        return find_k(input_list, start, first-1, k)


def quick_sort(input_list, start, end):
    pivot = end
    first = start
    last = end - 1
    print input_list, input_list[first], input_list[last], input_list[pivot]
    while first < last:
        while input_list[first] <= input_list[pivot] and first < last:
            first += 1
        while input_list[last] > input_list[pivot] and last > first:
            last -= 1
        if first < last:
            tmp = input_list[first]
            input_list[first] = input_list[last]
            input_list[last] = tmp
            first += 1
    if input_list[first] > input_list[pivot]:
        tmp = input_list[first]
        input_list[first] = input_list[pivot]
        input_list[pivot] = tmp

    if last - start > 1:
        quick_sort(input_list, start, first-1)
    if end - last > 1:
        quick_sort(input_list, first+1, end)

# a = [-1, 1, 4, 2, 5, 7, 9, 3, 6, 8]
# b = [1,2,3,4,5][::-1]
# # quick_sort(a, 0, len(a) - 1)
# # print a
# for i in range(1, len(a)+1):
#     print solution2(a, i)

def build_tree(self, start, end, curr):
    if start > end: return # empty list
    if start == end:
        self.seg_tree[curr] = self.nums[start]
    else:
        mid = start + (end - start)/2
        self.seg_tree[curr] = self.build_tree(start, mid, curr*2+1) + self.build_tree(mid+1, end, curr*2+2)
    return self.seg_tree[curr]