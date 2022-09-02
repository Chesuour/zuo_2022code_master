"""
Data : 2022/9/2
Author : SuquanChen
Address: yangzhou

定义何为step num？
比如680, 680+68+6=754,680的step num为754
给定一个正数num，判断他是不是某个数的step num
"""

class Solution:
    def stepNumber(num, one):
        tar = 0
        while num > 0:
            tar += num
            num //= 10
            print(num)
        if tar == one:
            return True
        else:
            return False


if __name__=="__main__":
    num = 680
    one = 754
    print(Solution.stepNumber(num, one))
