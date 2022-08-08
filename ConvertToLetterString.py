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
        if (index+1 )< len(string) and ((int(string[index]) - 0)+ (int(string[index+1]) -0) <27):
            res += Solution.process(string, index+2)
        return res
        
if __name__=="__main__":
    num = 1111
    print(Solution.ConvertToLetterString(num))