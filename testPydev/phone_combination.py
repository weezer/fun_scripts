class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        keyboard = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs',
                    '8': 'tuv', '9': 'wxyz'}
        result = []

        if len(digits) == 0:
            return []

        for i in digits:
            if len(result) == 0:
                result += list(keyboard[i])
                continue
            for j in range(len(result)):
                temp = result.pop(0)
                temp_list = keyboard[i]
                for z in temp_list:
                    result.append(temp + z)

        return result

if __name__ == "__main__":
    s = Solution()
    print s.letterCombinations("234")