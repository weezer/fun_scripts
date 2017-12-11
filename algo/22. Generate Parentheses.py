class Paretheses:
    def helper(self, l, r, item, result):
        if l > r:
            return
        if l == 0 and r == 0:
            result.append(item)
        if l > 0:
            self.helper(l-1, r, item + "(", result)
        if r > 0:
            self.helper(l, r-1, item + ")", result)

    def constructor(self, n):
        res = []
        self.helper(n, n, "", res)
        return res