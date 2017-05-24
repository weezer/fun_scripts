
class Solution:
    def __init__(self, input):
        self.test_string = input

    def read(self, n):
        temp_string = self.test_string[:n]
        self.test_string = self.test_string[n:]
        return temp_string

if __name__ == "__main__":
    s = Solution("abcdefg")
    print s.read(3)
    print s.read(2)
    print s.read(2)
