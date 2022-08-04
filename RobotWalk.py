"""
Data : 2022/8/4
Author : SuquanChen
Address: 出门问问 苏州

有一个机器人 在一个长度为1,2,3,4,5,6,....,n的列表上行走 在1只能走到2 在N只能走到N-1
其他位置可以左右随便走 现在给定初始位置、走的步数和目标值
有多少种走法
"""

class Solution():
    def __init__(self) -> None:
        pass

    def RobotWalk(arr, start, sum, aim):
        #arr 列表 start 开始的位置 sum 一共走几步 aim 走到的位置
        dp = [[-1]*(arr+1)]*(sum+1) 
        # print(dp)
        # print(Solution.pro~ocess2( start, sum, aim, arr,dp)) 
        print(Solution.process3(arr, start, aim, sum))

    def process(curr, res, aim, N):
        if res == 0:
            return 1 if curr == aim else 0
        if curr == 1:
            return Solution.process(2, res-1, aim, N)
        elif curr == N:
            return Solution.process(N-1, res-1, aim, N)
        else:
            return Solution.process(curr-1, res-1, aim, N) + Solution.process(curr+1, res-1, aim, N)

    
    #由第一块代码我们可以知道，结果和列表长度和步数相关
    #比如 要求列表长度为7，目标为9
    #（6,8）+（8,8）---> (5,7)+(7,7)+(7,7)+(9,7)
    #可以看出（7,7）算了两遍，那我们我们可以使用空间来节约时间的消耗
    #用dp[][]来存储每一个递归的值
    #空间换时间
    def process2(curr, res, aim, N,dp):
        if dp[curr][res] != -1:
            return dp[curr][res]
        ans = 0
        if res == 0:
            ans = 1 if curr == aim else 0
        if curr == 1:
            ans = Solution.process(2, res-1, aim, N)
        elif curr == N:
            ans = Solution.process(N-1, res-1, aim, N)
        else:
            ans = Solution.process(curr-1, res-1, aim, N) + Solution.process(curr+1, res-1, aim, N)
        dp[curr][res] = ans
        return ans

    def process3(N, start, aim, K):
        dp = [[0]*(N+1)]*(K+1)
        dp[aim][0] = 1
        for i in range(1,K):#列
            dp[1][i] = dp[2][i-1]
            for j in range(2,N-1):
                dp[j][i] = dp[j-1][i-1] + dp[j+1][i-1]
            dp[N][i] = dp[N-1][i-1]
        return dp[start][K]




    
if __name__ == "__main__":
      print(Solution.RobotWalk(4, 2, 4, 4))

    