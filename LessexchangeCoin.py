"""
Data : 2022/8/14
Author : SuquanChen
Address: 出门问问 苏州

换钱最少的货币数
《程序员算法面试指南》题目

=============================================================================================
PAY ATTENTION!!!!!!!!!!

n = 3
m = 3
dp = [[0] * n] * m
dp[0][1] = 1
print dp
# output:
# [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
matrix = [array] * 3
也就是说matrix = [array] * 3操作中 只是创建3个指向array的引用 所以一旦array改变matrix中3个list也会随之改变。
那如何才能在python中创建一个二维数组呢
例如创建一个3*3的数组
方法1 直接定义

[py]matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]][/py]

方法2 间接定义

matrix = [[0 for i in range(3)] for i in range(3)]
"""

class Solution():
    def LessExchangeCoin(arr, aim):
        return Solution.process(arr, 0, aim)
    def process(arr, index, rest):
        N = len(arr)
        if index ==N:
            return 0 if rest ==0 else -1
        res = -1
        k = 0
        while k * arr[index] <= rest:
            next = Solution.process(arr, index+1, rest - k * arr[index])
            if next != -1:
                res = next + k if res == -1 else min(res , next+k)
            k +=1
        return res
    

    def LessExchangeCoin_dp(arr, aim):
        N = len(arr)
        if not arr or N ==0 or aim < 0:
            return -1
        dp = [[0 for i in range(aim+1)]for j in range(N+1)]
        for j in range(1,aim+1):
            dp[N][j] = -1
        for i in range(N-1,-1,-1):
            for j in range(0,aim+1):
                dp[i][j] = -1
                if dp[i+1][j]!=-1:
                    dp[i][j] = dp[i+1][j]
                if j - arr[i] >=0 and dp[i][j - arr[i]]!=-1:
                    if dp[i][j] == -1:
                        dp[i][j] = dp[i][j - arr[i]] +1
                    else:
                        dp[i][j] = min(dp[i][j],dp[i][j - arr[i]]+1)
        print(dp) 
        return dp[0][aim]
if __name__=="__main__":
    arr, aim = [5,2,3], 20
    print(Solution.LessExchangeCoin(arr, aim))
    print(Solution.LessExchangeCoin_dp(arr, aim))
            