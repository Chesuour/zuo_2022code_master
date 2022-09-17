class Solution(object):
    def maxSumDivThree(nums):
        n = len(nums)
        dp = [[0] * 3 for _ in range(n+1)]
        dp[0][0] = 0
        dp[0][1] = float("-inf")
        dp[0][2] = float("-inf")
        for k in range(n):
            if nums[k] % 3 == 0: # k = 0 dp = 1
                dp[k+1][0] = max(dp[k][0], dp[k][0]+nums[k])
                dp[k+1][1] = max(dp[k][1], dp[k][1]+nums[k])
                dp[k+1][2] = max(dp[k][2], dp[k][2]+nums[k])
            elif nums[k] % 3 == 1:
                dp[k+1][0] = max(dp[k][0], dp[k][2]+nums[k])
                dp[k+1][1] = max(dp[k][1], dp[k][0]+nums[k])
                dp[k+1][2] = max(dp[k][2], dp[k][1]+nums[k])
            elif nums[k] % 3 == 2:
                dp[k+1][0] = max(dp[k][0], dp[k][1]+nums[k])
                dp[k+1][1] = max(dp[k][1], dp[k][2]+nums[k])
                dp[k+1][2] = max(dp[k][2], dp[k][0]+nums[k])
        return dp[-1][0]

if __name__ == "__main__":
    nums = [3,6,5,1,8]
    print(Solution.maxSumDivThree(nums))