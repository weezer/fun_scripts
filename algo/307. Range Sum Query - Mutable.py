import math


class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        len_nums = len(nums)
        segment_tree_length = math.pow(2, math.ceil(math.log(len_nums, 2))) * 2
        print segment_tree_length
        self.segment_tree = [0 for i in xrange(int(segment_tree_length))]
        print self.segment_tree
        self.nums = [0] + nums[:]
        print self.nums
        self.build_tree(1, len_nums, 1)

    def build_tree(self, start, end, curr):
        if start == end:
            self.segment_tree[curr] = self.nums[start]
            return self.segment_tree[curr]
        mid = (start + end) / 2
        self.segment_tree[curr] = self.build_tree(start, mid, curr*2) + self.build_tree(mid+1, end, curr*2+1)
        return self.segment_tree[curr]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """

    def __update(self, start, end, i, val):
        mid = end / 2

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        print len(self.nums)
        return self.__sum_range_calculate(1, len(self.nums)-1, i+1, j+1, 1)

    def __sum_range_calculate(self, start, end, sum_left, sum_right, curr):
        mid = (start + (end - start))/ 2
        if sum_left > end or sum_right < start:
            return 0
        elif sum_left >= start and end <= sum_right:
            return self.segment_tree[curr]
        else:
            return self.__sum_range_calculate(start, mid, sum_left, sum_right, curr * 2) + self.__sum_range_calculate(mid + 1, end, sum_left, sum_right, curr * 2 + 1)

        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # obj.update(i,val)
        # param_2 = obj.sumRange(i,j)

if __name__ == "__main__":
    s = NumArray([1,3,5,7,9])
    print s.segment_tree
    print s.sumRange(0,4)