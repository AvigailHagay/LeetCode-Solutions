class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        # sliding window technique
        start, end, max_length = 0, 0, 0
        window = set()

        while end < len(s):
            if s[end] not in window:
                window.add(s[end])
                end += 1
                max_length = max(max_length, end - start)
            else:
                window.remove(s[start])
                start += 1
        return max_length