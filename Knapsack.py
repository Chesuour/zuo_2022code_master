"""
Data : 2022/8/8
Author : SuquanChen
Address: 出门问问 苏州

背包问题
有 n 个物品和一个承重为 m 的背包. 给定数组 W表示每个物品的重量和数组 V 表示每个物品的价值。问最多能装入背包的总价值是多大?

例如：

n=5 m = 10, W = [2, 2, 6, 5,4], V = [6, 3, 5, 4,6]

结果为:15
"""

class Solution():
    """
    所有的货 重量和价值 都在w和v数组里
	为了方便 其中没有负数
	bag背包容量 不能超过这个载重
	返回：不超重的情况下，能够得到的最大价值
    """
    def Knapsack(W, V, bag):
        if not W and not V and len(W) != len(V) and len(W) == 0:
            return 0
        return Solution.process(W, V ,0, bag)

    # index 0~N
	# rest 负~bag
    def process(W, V, index, rest):
        if rest < 0:
            return -1
        if index == len(W):
            return 0
        p1 = Solution.process(W, V, index+1, rest)
        p2 = 0
        next = Solution.process(W, V, index+1, rest- W[index])
        if next != -1:
            p2 = V[index] + next
        return max(p1,p2)

    def Knapsack_dp(W, V, bag):
        if not W or not V or len(W) != len(V) or len(W) == 0:
            return 0
        N =len(W)
        bag_dp = [[0]*(bag+1)]*(N+1)
        for index in range(N-1,0,-1):
            for rest in range(bag,0,-1):
                p1 = bag_dp[index+1][rest]
                p2 = 0
                if rest - W[index] < 0:
                    next = -1
                else :
                    next = bag_dp[index+1][rest - W[index]]
                if next != -1:
                    p2 = V[index] + next
                bag_dp[index][rest] =  max(p1,p2)
        return bag_dp[0][bag]

if __name__=="__main__":
    W = [3, 2, 4, 7, 3, 1, 7]
    V = [5, 6, 3, 19, 12, 4, 2 ]
    bag = 15
    print(Solution.Knapsack(W, V, bag))
    print(Solution.Knapsack_dp(W, V, bag))

