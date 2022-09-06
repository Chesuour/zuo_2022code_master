"""
Data : 2022/9/6
Author : SuquanChen
Address: Yangzhou university

马跳棋盘问题
"""

class Solution():
    def HorseJump(a, b, k):
        return Solution.process(0, 0, k, a, b)

    def process(x: int, y: int, rest: int, a, b):
        if (x < 0) or (x > 9) or (y < 0) or (y > 8) :
            return 0
        if rest == 0:
            return 1 if (x == a and y == b) else 0

        ways =  Solution.process(x+1, y+2, rest-1, a, b)
        ways += Solution.process(x+2, y+1, rest-1, a, b)
        ways += Solution.process(x+2, y-1, rest-1, a, b)
        ways += Solution.process(x+1, y-2, rest-1, a, b)
        ways += Solution.process(x-1, y+2, rest-1, a, b)
        ways += Solution.process(x-2, y+1, rest-1, a, b)
        ways += Solution.process(x-1, y-2, rest-1, a, b)
        ways += Solution.process(x-2, y-1, rest-1, a, b)

        return ways

    def dp(a, b ,k):
        dp=[[[0 for n in range(11)] for n in range(10)]for n in range(k+2)]
        print(len(dp),len(dp[1]),len(dp[1][1]))
        dp[a][b][0]=1
        # print(dp)
        for rest in range(1,k+1):
            for x in range(10):
                for y in range(9):
                    ways =  Solution.get_dp(dp,x+1, y+2, rest-1)
                    ways += Solution.get_dp(dp,x+2, y+1, rest-1)
                    ways += Solution.get_dp(dp,x+2, y-1, rest-1)
                    ways += Solution.get_dp(dp,x+1, y-2, rest-1)
                    ways += Solution.get_dp(dp,x-1, y+2, rest-1)
                    ways += Solution.get_dp(dp,x-2, y+1, rest-1)
                    ways += Solution.get_dp(dp,x-1, y-2, rest-1)
                    ways += Solution.get_dp(dp,x-2, y-1, rest-1)
                    # print(x,y,rest)
                    dp[x][y][rest] = ways
        # print(dp)
        return dp[0][0][k]
    def get_dp(dp, x, y, rest):
        if (x < 0) or (x > 9) or (y < 0) or (y > 8) :
            return 0   
        return dp[x][y][rest]    
if __name__=="__main__":
    x, y, step = 7, 7, 10
    print(Solution.HorseJump(x, y, step))
    print(Solution.dp(x, y, step))