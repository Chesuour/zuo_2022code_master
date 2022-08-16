"""
Data : 2022/8/16
Author : SuquanChen
Address: 出门问问 苏州


返回一个数组中 子数组最大累计和 有负数
leetcode 53题
"""

class Solution():
    def SubArrayMax(arr):
        if not arr:
            return 0
        # max1, cur = 0, 0
        pre, maxm = arr[0], arr[0]
        for i in range(len(arr)):
            p1 = arr[i]
            p2 = arr[i] + pre
            cur = max(p1,p2)
            maxm = max(maxm , cur)
            pre = cur

            # cur += arr[i]
            # max1 = max(max1, cur)
            # cur = 0 if cur < 0 else cur
        return maxm




if __name__=="__main__":
    arr = [-3, 4, 5, 2, 1, 6, -1]
    print(Solution.SubArrayMax(arr))