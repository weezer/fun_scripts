class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        alphabet = {}
        word_len = 0
        max_word = 0
        for pos in range(len(s)):
            letter_pos = alphabet.get(s[pos])
            if letter_pos is not None:
                left = max(left, letter_pos + 1)
                word_len = pos - left
            alphabet[s[pos]] = pos
            word_len += 1
            max_word = max(max_word, word_len)
        return max_word


if __name__ == "__main__":
    s = Solution()
    print s.lengthOfLongestSubstring("abba")