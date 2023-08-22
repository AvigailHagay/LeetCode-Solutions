class Solution(object):
    def numRollsToTarget(self, n, k, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [[0] * (target+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            for j in range(1, k+1):
                for t in range(j, target+1):
                    dp[i][t] = (dp[i][t] + dp[i-1][t-j]) % MOD
        return dp[n][target]
