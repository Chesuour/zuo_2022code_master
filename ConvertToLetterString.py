"""
Data : 2022/8/8
Author : SuquanChen
Address: 出门问问 苏州

规定1和A对应、2和B对应、3和C对应.
那么一个数字字符串比如"111"就可以转化为:
"AAA"、 "KA"和"AK"
给定一个只有数字字符组成的字符串str 返回有多少种转化结果
"""

class Solution():
    def ConvertToLetterString(num):
        string= str(num)
        if not string or string == "":
            return 0
        return Solution.process(string,0)

    def process(string,index):
        if len(string) == index:
            return 1
        if string[index] == '0':
            return 0
        res = Solution.process(string, index+1)
        if (index+1 )< len(string) and (int(string[index])*10+ int(string[index+1]) <27):
            res += Solution.process(string, index+2)
        print(res)
        return res

    def ConvertToLetterString_dp(num):
        string= str(num)
        N = len(string)
        if string == None or N == 0:
            return 0
        dp = [0]*(N+1)
        dp[N] = 1
        res = 0
        # range(N-1,-1,-1) 是从N-1～0，如果是range(N-1,-1,-1)，则就是N-1～1，不包含0，注意python和java的区别
        for i in range(N-1,-1,-1):
            if string[i] !='0':
                res = dp[i+1]
                if (i+1 )< N and (int(string[i])*10+ int(string[i+1])  <27):
                    res += dp[i+2]
                dp[i] = res
        print(dp)
        return dp[0]

        
if __name__=="__main__":
    num = 1111
    print(Solution.ConvertToLetterString(num))
    print(Solution.ConvertToLetterString_dp(num))