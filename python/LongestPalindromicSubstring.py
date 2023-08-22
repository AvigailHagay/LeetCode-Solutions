class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        max_len = 0
        start = 0
        for i in range(n):
            
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > max_len:
                max_len = r - l - 1
                start = l + 1
        
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > max_len:
                max_len = r - l - 1
                start = l + 1

        return s[start:start + max_len]
