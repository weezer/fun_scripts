class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        len_s = len(s)
        len_word = len(words[0])
        word_count = len(words)
        words_map = dict([(name, words.count(name)) for name in words])
        r_answer = []
        for i in range(len_word):
            count = 0
            left = i
            right = i
            inside_count = word_count
            inside_map = {}
            while right < len_s:
                if words_map.get(s[right:right+len_word]) is not None:
                    if inside_map.get(s[right:right+len_word]) is None:
                        inside_map[s[right:right+len_word]] = 1
                        


